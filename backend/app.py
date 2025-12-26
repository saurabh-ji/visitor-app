from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host=os.environ["database-1.cxmui8ykwz3e.eu-west-1.rds.amazonaws.com"],
        user=os.environ["admin"],
        password=os.environ["saurabh123"],
        database=os.environ["societydb"]
    )

@app.route("/api/visitor", methods=["POST"])
def add_visitor():
    data = request.json

    db = get_db()
    cur = db.cursor()
    cur.execute("""
        INSERT INTO visitors
        (visitor_name, mobile, flat_number, visit_purpose)
        VALUES (%s, %s, %s, %s)
    """, (
        data["name"],
        data["mobile"],
        data["flat"],
        data["purpose"]
    ))
    db.commit()

    return jsonify({"status": "Visitor added"})
