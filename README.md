# Dash on flask with flask_login
An example of a seamless integration of a Dash app into an existing Flask app based on the application factory pattern.

For details and how to use, please read: [How to embed a Dash app into an existing Flask app](https://medium.com/@olegkomarov_77860/how-to-embed-a-dash-app-into-an-existing-flask-app-ea05d7a2210b)

## Deploy on Heroku (free)
First, edit the app.json and replace the value of the `repository`:
```
"repository": "https://github.com/okomarov/dash_on_flask"
```
with the URL to the forked repository.

Then click on the button:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)


## my readme's
## pg_config executable not found - while building venv
--did not happen 2nd time
SO solution 
$brew install postgresql

## error running flask db init | flask db migrate -m 'init'

flask db init
    ```Error: Directory migrations already exists and is not empty```
    
flask db migrate -m 'init'
    ```ERROR [alembic.env] Target database is not up to date.```
    ```ERROR [root] Error: Target database is not up to date.```
flask db upgrade

SO solution for alembic shiz:
$ flask db stamp head -fixed the issue
$ flask db migrate
$ flask db upgrade

SO solution detailed here
[https://flask-migrate.readthedocs.io/en/latest/]:

$ flask db init
This will add a migrations folder to your application. The contents of this folder need to be added to version control along with your other source files.

You can then generate an initial migration:

$ flask db migrate -m "Initial migration."
