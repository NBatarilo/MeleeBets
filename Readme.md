# Melee Bets

## Setup Instructions

### Docker

- Install Docker from [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Run the following command on your local 
``` 
docker run --name melee-bets \
    -p 5432:5432 \
    -e POSTGRES_DB=melee-bets \
    -e POSTGRES_PASSWORD=secret \
    -d postgres
```

### Flask
Ensure you have python installed with pip and venv modules installed globally
- Create a virtual environment with `python3 -m venv [whatever your venv name]`
- Then go into `bin/` and run `source activate` (on macOS)
- CD into the `backend` folder and run `pip install -r requirements.txt`
- To run the backend run `sh test.sh`

### Angular App
Ensure you have npm and node installed
- Install Angular Cli by running `npm install -g @angular/cli`
- Run `npm ci` in the `frontend` directory
- To start the angular app run `ng serve -o`