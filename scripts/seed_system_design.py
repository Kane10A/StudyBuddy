import sqlite3
import os
from datetime import datetime
from src.db.db_init import DB_PATH, db_init

SYSTEM_DESIGN_PROBLEMS = [
    ("Design a URL shortening service like TinyURL.",
     "Design a url shortening system where users input a URL and can shorten it ",
     "Easy",
     "https://www.hellointerview.com/learn/system-design/problem-breakdowns/bitly"
     ),
    ("Deisgn Dropbox - a file hosting service.",
     "Design a file hosting service where users can store files and share files",
     "Easy",
     "https://www.hellointerview.com/learn/system-design/problem-breakdowns/dropbox"
     ),
    ("Design Ticketmaster - an event ticketing platform.","","Medium","https://www.hellointerview.com/learn/system-design/problem-breakdowns/ticketmaster"),
    ("Design Whatsapp - a messaging application.","","Medium","https://www.hellointerview.com/learn/system-design/problem-breakdowns/whatsapp"),
    ("Design LeetCode ","","Medium","https://www.hellointerview.com/learn/system-design/problem-breakdowns/leetcode"),
    ("Design a web crawler.","","Hard","https://www.hellointerview.com/learn/system-design/problem-breakdowns/web-crawler"),
    ("Design Tinder.","Design a ","Hard","https://www.hellointerview.com/learn/system-design/problem-breakdowns/tinder"),
    ("Design a ride-sharing service like Uber or Lyft.","","Hard","https://www.hellointerview.com/learn/system-design/problem-breakdowns/uber"),
    ("Design a post search engine.","","Hard","https://www.hellointerview.com/learn/system-design/problem-breakdowns/fb-post-search"),
    ("Design an Ad Click Aggregator System.","","Hard","https://www.hellointerview.com/learn/system-design/problem-breakdowns/ad-click-aggregator"),
    ("Design a Rate Limiter","","Easy","https://www.hellointerview.com/learn/system-design/problem-breakdowns/rate-limiter")

]

def create_dict_from_tuple(problem_tuple):
    return {
        "title": problem_tuple[0],
        "statement": problem_tuple[1],
        "difficulty": problem_tuple[2],
        "tags": "System Design",
        "source": "HelloInterview",
        "link": problem_tuple[3] if len(problem_tuple) > 3 else None,
        "created_at": datetime.now().isoformat()
    }



def insert_into_db(cursor, problem_data):
    try:
        cursor.execute("""
            INSERT INTO problems (title, statement, difficulty, tags, source, link, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            problem_data['title'],
            problem_data['statement'],
            problem_data['difficulty'],
            problem_data['tags'],
            problem_data['source'],
            problem_data['link'],
            problem_data['created_at']
        ))

        print(f"Inserted problem: {problem_data['title']}")
    except sqlite3.Error as e:
        print(f"Error inserting into database: {e}")
    

def main():
    conn = sqlite3.connect(DB_PATH)
    db_init()
    try:
        cursor = conn.cursor()
        for problem in SYSTEM_DESIGN_PROBLEMS:
            parsed = create_dict_from_tuple(problem)
            insert_into_db(cursor, parsed)
        conn.commit()
    finally:
        if conn:
            conn.close()




if __name__ == "__main__":
    main()