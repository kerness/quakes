# dump the database

# load variables
export $(grep -v '^#' ../.env | xargs) 2> /dev/null

# dump database
docker compose exec db sh -c "pg_restore postgresql://${POSTGRES_USER}:${POSTGRES_PASS}@localhost:${PG_PORT}/quakes --data-only -d quakes --table quakes_quake .quakes.sql"
