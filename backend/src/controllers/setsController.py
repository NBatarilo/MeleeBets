import requests
from flask import Flask, jsonify, request, make_response
from src.auth import AuthError, requires_auth
from flask import Blueprint
from flask import current_app as app
from src.models import db, User, Player, Set, Tournament, Bet, UserBet, BetSchema

sets_bp = Blueprint(
    'sets_bp', __name__
)
#1271790 (nightclub phase_id)
def execute_query(tournament_slug, event_id = None, phase_id = None):
    url = "https://api.start.gg/gql/alpha"
    if phase_id is not None:
        with open('src/startggQueries/phaseSets.txt', 'r') as file:
            file_text = file.read().replace('<phase_id>', phase_id)

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
        

@sets_bp.route('/api/sets/<tournament_slug>', methods = ['GET'])
def get_sets(tournament_slug):
    return
    #What info to grab?
    #player_one name, player_two name, round, outcome, player_one sponsor, p2 sponsor
    

@sets_bp.route('/api/startgg/<tournament_slug>', methods = ['GET'])
def query_startgg(tournament_slug):

    url = "https://api.start.gg/gql/alpha"

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
    if tournament is None:
        tourneyInfo_response = execute_query(tournament_slug, event_id)
        #Add logic to insert to db
    

    #Got tourney info working! Next step is looking at docs to add other info to query. (I think date is the only thing)
    top8_phase = phase_ids[-1]["id"]
    phaseSets_response = execute_query(tournament_slug, event_id, top8_phase)

    return make_response(
    phaseSets_response.json(),
    phaseSets_response.status_code
    )


    """
    
    #Read query into string from file
    #TODO: Get phase ID's first, use last one to query for sets
    #Will be strictly getting top 8 from majors essentially. Read sets into db and query into tree for front end.
    #Could do SetNode object that has the set + parent set and children sets in list
    #ROUND AND IDENTIFIER WILL BE HUGE HERE. Gives us the tree structure
    with open('src/startggQueries/phaseSets.txt', 'r') as file:
        #Eventually this will use the "phases" query to get the phase ids. Rn this is for testing
        query = file.read().replace('<tournament_slug>', tournament_slug)

    #Build json payload/request and send request, jsonify response
    payload = {"query": query}
    
    headers = {"Authorization" : "Bearer 3b70dc3e655754d9010c3ea829e81cd8"}
    response = requests.post(url, json=payload, headers = headers)
    
    
    return make_response(
        response.json(),
        response.status_code
    )
    
    #Iterate through data and enter into db
    phase_id = response.json()["data"]["phase"]["id"]
    set_list = response.json()["data"]["phase"]["sets"]["nodes"]

        

    #for set in set_list:



    #return
    """


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