app = pyxo

build:
	docker build -t $(app) .

run:
	docker run --detach -p 8000:8000 $(app)

kill:
	docker ps | grep $(app) | awk '{print $$1}' | xargs docker kill
