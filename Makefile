ifneq (,$(wildcard ./.env))
	include .env
	export
	ENV_FILE_PARAM = --env-file .env
endif

build:
	docker compose up --build -d --remove-orphans
rebuild:
	docker compose down && docker-compose up --build -d --remove-orphans
up:
	docker compose up -d
down:
	docker compose down
logs:
	docker compose logs
migrate:
	docker compose exec api python manage.py migrate --noinput
makemigrations:
	docker compose exec api python manage.py makemigrations quakes --noinput
superuser:
	docker compose exec api python manage.py createsuperuser
down-v:
	docker compose down -v
shell:
	docker compose exec api python manage.py shell
flush:
	docker compose exec api python manage.py flush
lUSGS:
	docker compose exec api python manage.py loadUSGS
lGRSS:
	docker compose exec api python manage.py loadGRSS
