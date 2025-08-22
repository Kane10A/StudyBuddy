import sqlite3
import os
import pytest
from app.db_init import DB_PATH, db_init

TEST_DB_PATH = "test_db.sqlite"

@pytest.fixture(scope="module")
def setup_database():
    """
    Fixture to set up the database before tests and tear it down after.
    """
    # Ensure the database file does not exist before initialization
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)
    
    from app import db_init as db
    original_db_path = db.DB_PATH
    db.DB_PATH = TEST_DB_PATH

    # Initialize the database
    db_init()

    yield db

    # Teardown: remove the database file after tests
    db.DB_PATH = original_db_path
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)

def test_db_initialization(setup_database):
    """
    Test to ensure the database is initialized correctly.
    """
    db = setup_database
    assert os.path.exists(TEST_DB_PATH), "Database file should exist after initialization."

    # Check if the tables were created
    connection = sqlite3.connect(TEST_DB_PATH)
    cursor = connection.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    expected_tables = {'problems', 'solutions', 'attempts', 'feedback'}
    actual_tables = {table[0] for table in tables if not table[0].startswith('sqlite_')}

    assert actual_tables == expected_tables, f"Database tables were not created as expected. actual {actual_tables}"

    connection.close()

def test_problems_table_schema(setup_database):
    """
    Test to ensure the problems table schema is correct.
    """
    pass