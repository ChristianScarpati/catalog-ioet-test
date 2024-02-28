compose_command ?= docker-compose
docker_compose_file_path ?= infrastructure/docker/docker-compose.dev.yml
app_service ?= ioet-catalog-backend

.PHONY: help
help: ## Show this help (usage: make help)
	@echo "Usage: make [target]"
	@echo "Targets:"
	@awk '/^[a-zA-Z0-9_-]+:.*?##/ { \
		helpMessage = match($$0, /## (.*)/); \
		if (helpMessage) { \
			target = $$1; \
			sub(/:/, "", target); \
			printf "  \033[36m%-20s\033[0m %s\n", target, substr($$0, RSTART + 3, RLENGTH); \
		} \
	}' $(MAKEFILE_LIST)


.PHONY: build
build:	## Build project with docker-compose
	${compose_command} --build -d

.PHONY: up
up:	## Run all services locally
	${compose_command} -f ${docker_compose_file_path} up -d

.PHONY: clean
clean:	## Remove everything
	${compose_command} -f ${docker_compose_file_path} down --volumes --remove-orphans --rmi all

.PHONY: logs
logs:	## Show logs of all services
	${compose_command} -f ${docker_compose_file_path} logs -f
	
.PHONY: dev_shell
dev_shell:	## Run a dev shell
	@${compose_command} -f ${docker_compose_file_path} exec ${app_service} bash
