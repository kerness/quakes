# Project overview

Quakes is a web-based system for the acquisition, processing, and visualisation of geodata containing location and earthquake parameter information. System is based on a microservices architecture and the system's components are containerized using Docker software. 

Backend was created using Django with DjangoRestFramework for the REST API. Python was used to develop a module for exporting and processing data taken from USGS and GRSS.

Frontend was implemented using React. 


![name](https://github.com/kerness/quakes/blob/master/examples/usgs-all.png)
![name](https://github.com/kerness/quakes/blob/master/examples/usgs-circle.png)

# How to run this project

Clone this repo

    git clone https://github.com/kerness/quakes.git
    cd quakes

Create the .env file based on .env.example

    POSTGRES_USER=pguser
    POSTGRES_PASS=pgpass
    POSTGRES_DBNAME=quakes
    PG_HOST=db
    PG_PORT=5432
    SECRET_KEY=<provide django secret key>
    DEBUG=TRUE
    ALLOWED_HOSTS=<eg: localhost 127.0.0.1 [::1]>

Build the containers

    make build

Create migrations

    make makemigrations

Migrate

    make migrate
 
Load recent USGS and GRSS data

    make lUSGS && make lGRSS


Open web browser and go to localhost:8080
