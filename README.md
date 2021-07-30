# Pokemon Search

A simple 2 endpoint api to search for pokemon by name

Language - Python

Framework - FastAPI

## Clone project

```
$ git clone https://github.com/Lucx14/pokemon-search.git
$ cd pokemon-search
```

## To run with Docker

```
$ docker build -t pokemon-search-image .
$ docker run -d --name pokemon-search-container -p 80:80 pokemon-search-image
```

Then use Postman or a browser window to search for pokemon at these endpoints

> http://localhost:80/pokemon/mewtwo

> http://localhost:80/pokemon/translated/mewtwo

To Access the api documentation in a browser window

> http://localhost:80/docs

To run the tests whilte the container is running:

```
$ docker exec pokemon-search-container /bin/sh -c "pytest"
```

And if you want to run test in interactive mode:

```
$ docker exec -it pokemon-search-container /bin/sh
$ pytest -v
$ exit
```

To clear up you docker environment:

```
$ docker container stop pokemon-search-container
$ docker container rm pokemon-search-container
$ docker image rm pokemon-search-image
```

---

The requirements asked about changes or improvements if this was to be a production api. I would think about looking into caching api responses so that if a user requested the same name multiple times, my api would not need to call the poke api every time, same for the translator. And I would have another look at my error handling in the api clients because at the moment I raise exceptions specifically for a not found 404 or anything that is not a 200 response code so I think there is room for improvement there.
