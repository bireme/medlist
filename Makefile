IMAGE_NAME=bireme/medlist
APP_VERSION=$(shell git describe --tags --long --always | sed 's/-g[a-z0-9]\{7\}//')
TAG_LATEST=$(IMAGE_NAME):latest

COMPOSE_FILE_DEV=docker-compose-dev.yml
COMPOSE_FILE_API=docker-compose-api.yml

## variable used in docker-compose for tag the build image
export IMAGE_TAG=$(IMAGE_NAME):$(APP_VERSION)

tag:
	@echo "IMAGE TAG:" $(IMAGE_TAG)

## docker-compose desenvolvimento
dev_build:
	@docker-compose -f $(COMPOSE_FILE_DEV) build

dev_run:
	@docker-compose -f $(COMPOSE_FILE_DEV) up

dev_start:
	@docker-compose -f $(COMPOSE_FILE_DEV) up -d

dev_stop:
	@docker-compose -f $(COMPOSE_FILE_DEV) stop

dev_logs:
	@docker-compose -f $(COMPOSE_FILE_DEV) logs -f


dev_ps:
	@docker-compose -f $(COMPOSE_FILE_DEV) ps

dev_rm:
	@docker-compose -f $(COMPOSE_FILE_DEV) rm -f

dev_sh:
	@docker-compose -f $(COMPOSE_FILE_DEV) exec medlist sh

dev_make_test:
	@docker-compose -f $(COMPOSE_FILE_DEV) exec medlist make test

dev_migrate:
	@docker-compose -f $(COMPOSE_FILE_DEV) exec -T medlist python manage.py migrate


## docker-compose prod
prod_build:
	@docker-compose --compatibility build
	@docker tag $(IMAGE_TAG) $(TAG_LATEST)

prod_run:
	@docker-compose --compatibility up

prod_start:
	@docker-compose --compatibility up -d

prod_stop:
	@docker-compose --compatibility stop

prod_logs:
	@docker-compose --compatibility logs -f

prod_ps:
	@docker-compose --compatibility ps

prod_rm:
	@docker-compose --compatibility rm -f

prod_exec_shell:
	@docker-compose --compatibility exec medlist sh

prod_exec_collectstatic:
	@docker-compose --compatibility exec -T medlist python manage.py collectstatic --noinput

prod_migrate:
	@docker-compose --compatibility exec -T medlist python manage.py migrate

prod_make_test:
	@docker-compose --compatibility exec -T medlist make test
