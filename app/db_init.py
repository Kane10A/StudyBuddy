import sqlite3

DB_PATH = "db/study_budy.db"

def db_init():
    """
    Function to initialize the database.
    Creates a connection to the SQLite database and sets up the necessary tables.
    """
    try:
        # Create the database 
        dbConnection = sqlite3.connect(DB_PATH)

        # Cursor Object to help execute sql queries 
        cursor = dbConnection.cursor()
        print("DB Init")
        # Create the problems table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS problems (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    statement TEXT NOT NULL,
                    difficulty TEXT NOT NULL,
                    tags TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )""")
        # Create the solutions table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS solutions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    problem_id INTEGER NOT NULL,
                    solution_type TEXT NOT NULL,
                    solution_content TEXT NOT NULL,
                    language TEXT NOT NULL,
                    intuition TEXT NOT NULL,
                    performance_notes TEXT, 
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (problem_id) REFERENCES problems(id) ON DELETE CASCADE
                    )""")

        # Create the attempts table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS attempts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    problem_id INTEGER NOT NULL,
                    attempt_type TEXT NOT NULL,
                    attempt_content TEXT NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (problem_id) REFERENCES problems(id) ON DELETE CASCADE
                       )""")

        # Create the feedback table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       attempt_id INTEGER NOT NULL,
                       problem_id INTEGER NOT NULL,
                       correctness TEXT NOT NULL,
                       clarirty TEXT NOT NULL,
                       feedback_content TEXT NOT NULL,
                       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                       FOREIGN KEY (attempt_id) REFERENCES attempts(id) ON DELETE CASCADE,
                       FOREIGN KEY (problem_id) REFERENCES problems(id) ON DELETE CASCADE
                       )""")
        
        dbConnection.commit()
        print("Database initialized successfully.")
        
    except sqlite3.Error as error:
        print("Error occured - ", error)
    #Close the connection 
    finally:
        if dbConnection:
            dbConnection.close()
            print("Closing Connection")

def seed_sample_data():
    """
    Function to seed the database with sample data.
    This function is currently empty and can be implemented as needed.
    """
    # Example of how to insert sample data
    # dbConnection = sqlite3.connect(DB_PATH)
    # cursor = dbConnection.cursor()
    # cursor.execute("INSERT INTO problems (title, statement, difficulty, tags) VALUES (?, ?, ?, ?)", 
    #                ("Sample Problem", "This is a sample problem statement.", "Easy", "sample,example"))
    # dbConnection.commit()
    # dbConnection.close()
    pass
