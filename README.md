# About

This repo contains my engineering thesis. Graduated in January 2023 with engineer's (bachelor's) degree. AGH UST. 

# Project overview

Quakes is a web-based system for the acquisition, processing, and visualisation of geodata containing location and earthquake parameter information. System is based on a microservices architecture and the system's components are containerized using Docker software. 

Backend was created using Django with DjangoRestFramework for the REST API. Python was used to develop a module for exporting and processing data taken from USGS and GRSS.

Frontend is a WebGIS application implemented using React and Leaflet for mapping.


![name](https://github.com/kerness/quakes/blob/master/examples/usgs-all.png)
![name](https://github.com/kerness/quakes/blob/master/examples/usgs-circle.png)

# Data sources

Data comes drom two sources:
- United States Geological Survey (USGS) Earthquake Catalog API (https://earthquake.usgs.gov/fdsnws/event/1/)
- Górnośląska Regionalna Sieć Sejsmologiczna (GRSS) (https://grss.gig.eu/)

*data_fetchers* python module was implemented to obtain data from sources.
- *USGSQuakesExporter* and *USGSFetcher* - API wrappers to get historical data and data from last month (updating)
- *GRSSFetcher* - web scrapper


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
