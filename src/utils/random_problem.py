import sqlite3
import random
from src.db.db_init import DB_PATH, db_init

def get_random_problems(number=5, difficulty=None, topic=None, source=None):
    conn = sqlite3.connect(DB_PATH)
    try:
        cursor = conn.cursor()
        query = f"SELECT title,  statement, difficulty, tags, source, link FROM problems ORDER BY RANDOM() LIMIT {number};"

        cursor.execute(query)
        result = cursor.fetchall()

        problems = []
        for row in result:
            problems.append({
                "title": row[0],
                "statement": row[1],
                "difficulty": row[2],
                "topic": row[3],
                "source": row[4],
                "url": row[5]
            })

        return problems
    finally:
        if conn:
            conn.close() 