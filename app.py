from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Blake Stoffel in 3308'

@app.route('/db_test')
def db_test():
	conn = psycopg2.connect("postgresql://flask_example_db_user:kXR53tAUv884FlsAFBXk51jy90Zgz9oq@dpg-dbpaahdbedkc7385vo9g-a.oregon-postgres.render.com/flask_example_db")
	conn.close()
	return "Database Connection Successful"

@app.route('/db_create')
def db_create():
	conn = psycopg2.connect("postgresql://flask_example_db_user:kXR53tAUv884FlsAFBXk51jy90Zgz9oq@dpg-dbpaahdbedkc7385vo9g-a.oregon-postgres.render.com/flask_example_db")
	cur = conn.cursor()
	cur.execute('''
	    CREATE TABLE IF NOT EXISTS Basketball(
	        First varchar(255),
	        Last varchar(255),
	        City varchar(255),
	        Name varchar(255),
	        Number int
	        );
	''')
	conn.commit()
	conn.close()
	return "Basketball Table Successfully Created"