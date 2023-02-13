import requests
from flask import Flask, jsonify, request, make_response, Blueprint
from src.auth import AuthError, requires_auth
from flask import current_app as app
from src.models import db, User, Player, Set, Tournament, Bet, UserBet, BetSchema, TournamentSchema
from datetime import datetime

sets_bp = Blueprint(
    'sets_bp', __name__
)
#1271790 (nightclub phase_id)
#Test slug: the-nightclub-s5e12-os-nyc
def execute_query(tournament_slug, event_id = None, phase_id = None):
    url = "https://api.start.gg/gql/alpha"
    if phase_id is not None:
        with open('src/startggQueries/phaseSets.txt', 'r') as file:
            file_text = file.read().replace('<phase_id>', str(phase_id))

    elif event_id is not None:
        with open('src/startggQueries/tourneyInfo.txt', 'r') as file:
            file_text = file.read().replace('<tournament_slug>', tournament_slug).replace('<event_id>', str(event_id))

    else:
        with open('src/startggQueries/eventInfo.txt', 'r') as file:
            file_text = file.read().replace('<tournament_slug>', tournament_slug)

    split_info = file_text.split(",\n")
    query = split_info[0]
    variables = split_info[1]
    
    payload = {"query": query, "variables": variables}
    headers = {"Authorization" : "Bearer 3b70dc3e655754d9010c3ea829e81cd8"}
    response = requests.post(url, json=payload, headers = headers)

    return response
        

@sets_bp.route('/api/sets/<tournament_slug>', methods = ['GET', 'POST'])
def sets_db_api(tournament_slug):
    if request.method == 'POST':
        return

    else:
        return
    #What info to grab?
    #player_one name, player_two name, round, outcome, player_one sponsor, p2 sponsor
    

@sets_bp.route('/api/sets/startgg/<tournament_slug>', methods = ['GET'])
def query_startgg(tournament_slug):

    #Add tournament to db if not present
    #For me - I think it will be 3 queries total. Event info to get event id and phase ids. Tourney info to get
    #touney db info. And then finally phaseSets to get all the stuff we actually want. 

    eventInfo_response = execute_query(tournament_slug)
    

    #Save event id and phase ids - then make tournament query. Phase query happens outside.
    #Thinking of changing model to include event and phase, but I can also just query eventInfo again if this if doesn't trigger
    event_id = eventInfo_response.json()["data"]["event"]["id"]
    phase_ids = eventInfo_response.json()["data"]["event"]["phases"]
    
    #Check if tourney exists
    tournament = db.session.query(Tournament).filter(Tournament.tournament_slug == tournament_slug).first()
    tournament_added = False

    if tournament is None:
        #Realizing now that this should redirect to a tournamentController. TODO
        tourneyInfo_response = execute_query(tournament_slug, event_id)
        #Add logic to insert to db
        name = tourneyInfo_response.json()["data"]["tournament"]["name"]
        start_date = datetime.fromtimestamp(tourneyInfo_response.json()["data"]["tournament"]["startAt"])
        end_date = datetime.fromtimestamp(tourneyInfo_response.json()["data"]["tournament"]["endAt"])
        num_entrants = tourneyInfo_response.json()["data"]["tournament"]["participants"]["pageInfo"]["total"]
        tournament_type = "TBD"

        new_tournament = Tournament(
            tournament_name = name,
            tournament_date_start = start_date,
            tournament_date_end = end_date,
            tournament_slug = tournament_slug,
            entrants_number = num_entrants,
            tournament_type = tournament_type,
            created_by = "Test"
        )

        db.session.add(new_tournament)
        db.session.commit()
        tournament_added = True

    if tournament_added:
        tournament = db.session.query(Tournament).filter(Tournament.tournament_slug == tournament_slug).first()

    tournament_result = TournamentSchema().dump(tournament)
    #return jsonify(tournament_result)
    
    #Finished adding tourney to and querying from db, next is adding the actual set functionality.
    #Going to execute phaseSets using previous phase_ids. Then add Sets and Players (where applicable) 
    top8_phase_id = phase_ids[-1]["id"]
    phaseSets_response = execute_query(tournament_slug, event_id, top8_phase_id)
    

    #Eventually going to have this redirect to the sets_db_api as a post
    set_list = phaseSets_response.json()["data"]["phase"]["sets"]["nodes"]

    #json parsing into db - yuck
    tournament_id = tournament.id
    for set in set_list:
        round = set["round"]
        identifier = set["identifier"]
        startgg_setID = set["id"]
        
        p1_info = set["slots"][0]
        p1_tag = p1_info["entrant"]["name"].split(" | ")
        p1_sponsor = p1_tag[0]
        p1_name = p1_tag[1]

        p2_info = set["slots"][1]
        p2_tag = p2_info["entrant"]["name"].split(" | ")
        p2_sponsor = p2_tag[0]
        p2_name = p2_tag[1]


        p1 = db.session.query(Player).filter(Player.player_name == p1_name).first()
        p2 = db.session.query(Player).filter(Player.player_name == p2_name).first()


        #Add players if not present in db
        if p1 is None:
            new_player_one = Player(
                player_name = p1_name,
                sponsor = p1_sponsor,
                region = "TBD",
                created_by = "Test"
            )
        db.session.add(new_player_one)

        if p2 is None:
            new_player_two = Player(
                player_name = p2_name,
                sponsor = p2_sponsor,
                region = "TBD",
                created_by = "Test"
            )
        db.session.add(new_player_two)
        db.session.commit()

        #TODO NEXT
        #Get prereq IDs for both players
        #Query players for IDs
        #Create Set and add to db

        

    return make_response(
    phaseSets_response.json(),
    phaseSets_response.status_code
    )
    




#Legacy code - keeping for now for syntax. This functionality prob going to not be an endpoint
#Is this the best way to do this? Maybe remove POST method entirely and move further to back end
#Need to add authentication if it stays
"""
@app.route('/matches', methods=['POST'])
def add_matches():
    
    posted_matches = request.get_json()

    matches = posted_matches["matches_array"]
 
    
    session = Session()
    for match in matches:
        MatchSchema(only=('player_one', 'player_two')).load(match)
        session.add(Match(match["player_one"], match["player_two"], created_by="HTTP post request"))
    
    session.commit()

   
    new_match = MatchSchema().dump(Match(matches[0]["player_one"], matches[0]["player_two"], created_by="HTTP post request"))
    session.close()
    #Return first match inserted
    return jsonify(new_match), 201
"""


"""
Example response for phase sets
{
    "actionRecords": [],
    "data": {
        "phase": {
            "id": 1271790,
            "name": "Bracket",
            "sets": {
                "nodes": [
                    {
                        "fullRoundText": "Losers Final",
                        "id": "preview_1949617_-6_0",
                        "identifier": "K",
                        "round": -6,
                        "slots": [
                            {
                                "entrant": null,
                                "id": "preview_1949617_-6_0-0",
                                "prereqId": "preview_1949617_3_0",
                                "prereqPlacement": 2,
                                "prereqType": "set"
                            },
                            {
                                "entrant": null,
                                "id": "preview_1949617_-6_0-1",
                                "prereqId": "preview_1949617_-5_0",
                                "prereqPlacement": 1,
                                "prereqType": "set"
                            }
                        ]
                    },
                    {
                        "fullRoundText": "Losers Semi-Final",
                        "id": "preview_1949617_-5_0",
                        "identifier": "J",
                        "round": -5,
                        "slots": [
                            {
                                "entrant": null,
                                "id": "preview_1949617_-5_0-0",
                                "prereqId": "preview_1949617_-4_0",
                                "prereqPlacement": 1,
                                "prereqType": "set"
                            },
                            {
                                "entrant": null,
                                "id": "preview_1949617_-5_0-1",
                                "prereqId": "preview_1949617_-4_1",
                                "prereqPlacement": 1,
                                "prereqType": "set"
                            }
                        ]
                    },
                    {
                        "fullRoundText": "Losers Quarter-Final",
                        "id": "preview_1949617_-4_0",
                        "identifier": "H",
                        "round": -4,
                        "slots": [
                            {
                                "entrant": null,
                                "id": "preview_1949617_-4_0-0",
                                "prereqId": "preview_1949617_2_1",
                                "prereqPlacement": 2,
                                "prereqType": "set"
                            },
                            {
                                "entrant": null,
                                "id": "preview_1949617_-4_0-1",
                                "prereqId": "preview_1949617_-3_0",
                                "prereqPlacement": 1,
                                "prereqType": "set"
                            }
                        ]
                    },
                    {
                        "fullRoundText": "Losers Quarter-Final",
                        "id": "preview_1949617_-4_1",
                        "identifier": "I",
                        "round": -4,
                        "slots": [
                            {
                                "entrant": null,
                                "id": "preview_1949617_-4_1-0",
                                "prereqId": "preview_1949617_2_0",
                                "prereqPlacement": 2,
                                "prereqType": "set"
                            },
                            {
                                "entrant": null,
                                "id": "preview_1949617_-4_1-1",
                                "prereqId": "preview_1949617_-3_1",
                                "prereqPlacement": 1,
                                "prereqType": "set"
                            }
                        ]
                    },
                    {
                        "fullRoundText": "Winners Round 1",
                        "id": "preview_1949617_1_1",
                        "identifier": "A",
                        "round": 1,
                        "slots": [
                            {
                                "entrant": {
                                    "id": 11935422,
                                    "name": "RadioNights"
                                },
                                "id": "preview_1949617_1_1-0",
                                "prereqId": "22739812",
                                "prereqPlacement": null,
                                "prereqType": "seed"
                            },
                            {
                                "entrant": {
                                    "id": 11935501,
                                    "name": "Kadence"
                                },
                                "id": "preview_1949617_1_1-1",
                                "prereqId": "22739906",
                                "prereqPlacement": null,
                                "prereqType": "seed"
                            }
                        ]
                    },
                    {
                        "fullRoundText": "Winners Round 1",
                        "id": "preview_1949617_1_3",
                        "identifier": "B",
                        "round": 1,
                        "slots": [
                            {
                                "entrant": {
                                    "id": 11935393,
                                    "name": "Arpeggi"
                                },
                                "id": "preview_1949617_1_3-0",
                                "prereqId": "22739783",
                                "prereqPlacement": null,
                                "prereqType": "seed"
                            },
                            {
                                "entrant": {
                                    "id": 11935549,
                                    "name": "PLAY SMS | wutang36genders"
                                },
                                "id": "preview_1949617_1_3-1",
                                "prereqId": "22739954",
                                "prereqPlacement": null,
                                "prereqType": "seed"
                            }
                        ]
                    },
                    {
                        "fullRoundText": "Winners Semi-Final",
                        "id": "preview_1949617_2_0",
                        "identifier": "C",
                        "round": 2,
                        "slots": [
                            {
                                "entrant": {
                                    "id": 11935341,
                                    "name": "Species"
                                },
                                "id": "preview_1949617_2_0-0",
                                "prereqId": "preview_1949617_1_0",
                                "prereqPlacement": 1,
                                "prereqType": "set"
                            },
                            {
                                "entrant": null,
                                "id": "preview_1949617_2_0-1",
                                "prereqId": "preview_1949617_1_1",
                                "prereqPlacement": 1,
                                "prereqType": "set"
                            }
                        ]
                    },
                    {
                        "fullRoundText": "Winners Semi-Final",
                        "id": "preview_1949617_2_1",
                        "identifier": "D",
                        "round": 2,
                        "slots": [
                            {
                                "entrant": {
                                    "id": 11935361,
                                    "name": "DERT | Legs"
                                },
                                "id": "preview_1949617_2_1-0",
                                "prereqId": "preview_1949617_1_2",
                                "prereqPlacement": 1,
                                "prereqType": "set"
                            },
                            {
                                "entrant": null,
                                "id": "preview_1949617_2_1-1",
                                "prereqId": "preview_1949617_1_3",
                                "prereqPlacement": 1,
                                "prereqType": "set"
                            }
                        ]
                    },
                    {
                        "fullRoundText": "Winners Final",
                        "id": "preview_1949617_3_0",
                        "identifier": "E",
                        "round": 3,
                        "slots": [
                            {
                                "entrant": null,
                                "id": "preview_1949617_3_0-0",
                                "prereqId": "preview_1949617_2_0",
                                "prereqPlacement": 1,
                                "prereqType": "set"
                            },
                            {
                                "entrant": null,
                                "id": "preview_1949617_3_0-1",
                                "prereqId": "preview_1949617_2_1",
                                "prereqPlacement": 1,
                                "prereqType": "set"
                            }
                        ]
                    },
                    {
                        "fullRoundText": "Grand Final",
                        "id": "preview_1949617_4_0",
                        "identifier": "F",
                        "round": 4,
                        "slots": [
                            {
                                "entrant": null,
                                "id": "preview_1949617_4_0-0",
                                "prereqId": "preview_1949617_3_0",
                                "prereqPlacement": 1,
                                "prereqType": "set"
                            },
                            {
                                "entrant": null,
                                "id": "preview_1949617_4_0-1",
                                "prereqId": "preview_1949617_-6_0",
                                "prereqPlacement": 1,
                                "prereqType": "set"
                            }
                        ]
                    },
                    {
                        "fullRoundText": "Grand Final Reset",
                        "id": "preview_1949617_4_1",
                        "identifier": "G",
                        "round": 4,
                        "slots": [
                            {
                                "entrant": null,
                                "id": "preview_1949617_4_1-0",
                                "prereqId": "preview_1949617_4_0",
                                "prereqPlacement": 1,
                                "prereqType": "set"
                            },
                            {
                                "entrant": null,
                                "id": "preview_1949617_4_1-1",
                                "prereqId": "preview_1949617_4_0",
                                "prereqPlacement": 2,
                                "prereqType": "set"
                            }
                        ]
                    }
                ],
                "pageInfo": {
                    "total": 11
                }
            }
        }
    },
    "extensions": {
        "cacheControl": {
            "hints": null,
            "version": 1
        },
        "queryComplexity": 56
    }
}
"""