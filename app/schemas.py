PROBLEMS_TABLE_SCHEMA = """
CREATE TABLE IF NOT EXISTS problems (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    statement TEXT NOT NULL,
    difficulty TEXT NOT NULL,
    tags TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
"""

SOLTIONS_TABLE_SCHEMA =  """
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
                    )"""

ATTEMPTS_TABLE_SCHEMA = """
        CREATE TABLE IF NOT EXISTS attempts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    problem_id INTEGER NOT NULL,
                    attempt_type TEXT NOT NULL,
                    attempt_content TEXT NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (problem_id) REFERENCES problems(id) ON DELETE CASCADE
                       )"""

FEEDBACK_TABLE_SCHEMA = """
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
                       )"""
