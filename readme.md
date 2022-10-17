# redis-full-template

This template counts with:
- Full _dockerization_
- FastAPI application structure
- Postgres database
- Redis cache (I recommend to use DataGrip or RedisInsight GUI for visualizing)
- Database adminer
- Logging configuration

# Getting started
1. Set environment variables
```
DB_USERNAME=
DB_PASSWORD=
REDIS_PASSWORD=
```

2. Create docker containers
```
docker-compose up
```

Wait for the database to accept connections to start using the API. If this is the first time you are launching the application and the database is being created, you may need to wait for the database to finish creating and restart the application.

_Note: when you want to stop it, remember to use `docker-compose down`_

You're done! You can explore the files I left to you. There is an example of how to create models, crud functions, dependencies (db and redis)
database engine creating, etc.
You can see the Swagger documentation in the endpoint `/docs` (If you're on a local environment, `localhost:8000/docs`).

Any questions or suggestions are welcome.

![perfect](https://media.tenor.com/JMr_dlDTHJIAAAAC/theboys-perfect.gif)