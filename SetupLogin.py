import sqlite3
from flask import Flask, request

app = Flask(__name__)

def create_connection(path):
 
  connection = None

  try:
    connection = sqlite3.connect(path)
  except sqlite3.Error as e:
    print(e)

  return connection

def execute_query(conn, query):
 

  cursor = conn.cursor()

  try:
    cursor.execute(query) 
    conn.commit() 

    return cursor
  except Error as e:
    print(e)

@app.route('/')
def create_table():
 
  conn = create_connection('players.sqlite')

  create_query = """
CREATE TABLE IF NOT EXISTS players (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE,
  password TEXT,
  highscore INTEGER DEFAULT 0
);
"""

  execute_query(conn, create_query)

  return "success"

@app.route('/signup', methods=['POST'])
def signup():
  body = request.json

  username = body['username']
  password = body['password']

  insert_query = f"""
INSERT INTO {username} {password}
"""  
@app.route('/highscore', methods=['POST'])
def insert_highscore():
    body = request.json

    highscore = body['highscore']
    username = body['username']

    update_query = f"""
UPDATE players
SET
   highscore = {highscore}
WHERE
   username = {username}
 """