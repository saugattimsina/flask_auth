# flask_auth
## A fully usable AUTHUNTICATION app in flask.. 



# steps to use 

pip insrall -r requirements.txt

## create role on postgres ..
CREATE USER xxxxx WITH PASSWORD 'password';

## create database name flask_app..

create database flask_app;


## edit config.py

# follow the following commands to execute

flask db init
flask db migrate -m "Initial migration."
flask db upgrade


# python exec.py