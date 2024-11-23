from flask import Flask, request, g
import sqlite3

app = Flask(__name__)

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('paste.db', detect_types=sqlite3.PARSE_DECLTYPES)
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def get_paste(id):
    db = get_db()
    body = db.execute("SELECT body FROM pastes WHERE id = ?", (id,)).fetchone()[0]
    return body

def store_paste(body):
    db = get_db()
    id = db.execute("INSERT INTO pastes (body) VALUES (?) RETURNING id", (body,)).fetchone()[0]
    db.commit()
    return id


@app.route("/paste/<id>", methods=["GET"])
def get_paste_route(id):
    paste_body = get_paste(id)
    return {"body": paste_body}

@app.route("/paste", methods=["POST"])
def new_paste_route():
    body = request.get_json()["body"]
    id = store_paste(body)
    return {"id": id}

@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*" # <- You can change "*" for a domain for example "http://localhost"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response

app.teardown_appcontext(close_db)