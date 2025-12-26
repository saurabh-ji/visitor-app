from flask import Flask, jsonify
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host=os.environ["database-1.cxmui8ykwz3e.eu-west-1.rds.amazonaws.com"],
        user=os.environ["admin"],
        password=os.environ["saurabh123"],
        database=os.environ["sitedb"]
    )

@app.route("/api/visit")
def visit():
    db = get_db()
    cur = db.cursor()

    cur.execute("UPDATE visitors SET count = count + 1 WHERE id = 1")
    db.commit()

    cur.execute("SELECT count FROM visitors WHERE id = 1")
    count = cur.fetchone()[0]

    return jsonify({"visitors": count})
