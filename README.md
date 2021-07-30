Pokemon Search

Framework - FastAPI
Language - Python

app runs on localhost:8000
localhost:8000
localhost:8000/pokemon/<pokemon-name>
localhost:8000/pokemon/translated/<pokemon-name>
docs available on localhost:8000/docs

to run in vscode with debugger open the debugger menu

- Run and Debug
- Select FastAPI
- enter path - app.main.py

run tests with pytest

Docker commands:
docker build -t pokemon-search-image .
docker run -d --name pokemon-search-container -p 80:80 pokemon-search-image

http://localhost:80/pokemon/mewtwo
http://localhost:80/pokemon/translated/mewtwo

To run tests
docker exec pokemon-search-container /bin/sh -c "pytest"

or interactively
docker exec -it pokemon-search-container /bin/sh
$ pytest -v

Clean up the docker environment
docker container stop pokemon-search-container
docker container rm pokemon-search-container
docker image rm pokemon-search-image
