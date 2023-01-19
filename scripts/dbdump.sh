# dump the database

# load variables
export $(grep -v '^#' ../.env | xargs) 2> /dev/null

# dump database
docker compose exec db sh -c "pg_dump postgresql://${POSTGRES_USER}:${POSTGRES_PASS}@localhost:${PG_PORT}/quakes > ~/quakes.sql"

# copy to local 
docker compose cp db:/root/quakes.sql ./quakes.sql