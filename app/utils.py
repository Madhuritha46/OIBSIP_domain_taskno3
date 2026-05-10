import sqlite3
from datetime import datetime


def create_database():

    conn = sqlite3.connect("fraud_logs.db")

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            prediction TEXT,
            probability REAL
        )
    """)

    conn.commit()

    conn.close()


def insert_log(prediction, probability):

    conn = sqlite3.connect("fraud_logs.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO logs (timestamp, prediction, probability)
        VALUES (?, ?, ?)
        """,
        (
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            prediction,
            probability
        )
    )

    conn.commit()

    conn.close()


def fetch_logs():

    conn = sqlite3.connect("fraud_logs.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM logs")

    rows = cursor.fetchall()

    conn.close()

    return rows
