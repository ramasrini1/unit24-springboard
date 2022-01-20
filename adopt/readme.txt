On terminal run these commands

python3 -m venv venv
source venv/bin/activate
pip3 install flask
pip3 install flask-debugtoolbar
pip3 install psycopg2
pip3 install flask-sqlalchemy
pip3 install flask-wtf
pip3 freze > requirements.txt

First create database on ven terminal run
createdb adopt

To run seed file
ipython3 > seed.py