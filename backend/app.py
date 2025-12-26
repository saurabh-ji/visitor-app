from flask import Flask
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
        database=os.environ["societydb"],
        port=3306
    )

@app.route("/")
def home():
    try:
        db = get_db()
        cur = db.cursor()
        cur.execute("SELECT DATABASE()")
        return f"Backend connected to DB ✅ : {cur.fetchone()[0]}"
    except Exception as e:
        return f"DB connection failed ❌ : {e}"
