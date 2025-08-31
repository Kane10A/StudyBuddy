import os
import re
import sqlite3
import sys
from datetime import datetime
import yaml
from src.db.db_init import DB_PATH, db_init

def extract_problem_from_notes(note_file_path: str):
    with open(note_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if content.startswith('---'):
        parts = content.split('---')
        if len(parts) >= 3:
            yaml_metadata = parts[1]
            content = parts[2]
        else:
            front_matter = ""
    else:
        yaml_metadata = ""

    metadata = yaml.safe_load(yaml_metadata) if yaml_metadata else {}
    tags = metadata.get('tags', [])


    leetcode_match = [t for t in tags if t.startswith('leetcode')] if tags else []
    
    if not leetcode_match:
        print(f"Skipping {note_file_path}: No leetcode tag found.")
        return None
    
    title_regex = regex_search(r'#\s*(.*?)\n', content)
    title = title_regex if title_regex else os.path.splitext(os.path.basename(note_file_path))[0]

    platform = regex_search(r"\* Platform:\s*(\w+)", content) or "LeetCode"
    difficulty = regex_search(r"\* Difficulty:\s*(\w+)", content)

    question_text = extract_problem_body(content)
    problem_link = regex_search(r"\* \[Problem Link\]\((https?://[^\)]+)\)", content)

    return {
        "title": title,
        "statement": question_text,
        "difficulty": difficulty if difficulty else "Unknown",
        "tags": ','.join(tags),
        "source": platform,
        "link": problem_link,
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
    
def regex_search(pattern, text, flags=0):
    match = re.search(pattern, text, flags)
    return match.group(1).strip() if match else None

def extract_problem_body(body_text):
    patterns = [
         r"##\s*(?:📝\s*)?Original Problem Statement\s*\n([\s\S]+?)(?:\n##|\Z)",
        r"##\s*(?:🔍\s*)?Problem Summary\s*\n([\s\S]+?)(?:\n##|\Z)"
    ]
    for pattern in patterns:
        match = re.search(pattern, body_text, re.IGNORECASE)
        if match:
            return match.group(1).strip()

    # If neither heading is found
    return ""

def main():
    if len(sys.argv) != 2:
        print("Usage: python import_obsidian.py <path_to_obsidian_notes>")
        sys.exit(1)

    notes_directory = sys.argv[1]
    if not os.path.isdir(notes_directory):
        print(f"Error: {notes_directory} is not a valid directory.")
        sys.exit(1)

    conn = sqlite3.connect(DB_PATH)
    db_init()
    try:
        cursor = conn.cursor() 
        for root, _, files in os.walk(notes_directory):
            for file in files:
                if file.endswith(".md"):
                    note_path = os.path.join(root, file)
                    problem_data = extract_problem_from_notes(note_path)
                    if problem_data:
                        insert_into_db(cursor, problem_data)
        conn.commit()
        conn.close()
        print("All problems imported successfully.")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    main()