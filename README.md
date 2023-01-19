To run this project locally:

Clone repo and cd into

Create the .env file based on .env.example

Build the containers
make build

Create migrations
make makemigrations

Migrate
make migrate

Load recent USGS and GRSS data
make lUSGS && make lGRSS

Open web browser and go to localhost:8080

