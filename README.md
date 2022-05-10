This is a small Python Flask App that uses PostgressDB to store covid19 country and state's data.

Setup steps as follows:

1. Create a virtual environment from the CMD:

   > cd covid19-backend
   > py -3 -m venv venv

2. Activate the Environment with the following command:

   > venv\Scripts\activate

3. When done with the environment, install following from the CMD:
   3.1 Flast - pip install Flask
   3.2 psycopg2 - for interacting with Postgres - pip install psycopg2

Once all these are installed and Python 3+ is installed and postgress+pgAdmin, then all should be set for starting the application with the following commands from the CMD.

> set FLASK_APP=app
> flask run
