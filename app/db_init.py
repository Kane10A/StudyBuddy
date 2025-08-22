import sqlite3
from .schemas import PROBLEMS_TABLE_SCHEMA, SOLUTIONS_TABLE_SCHEMA, ATTEMPTS_TABLE_SCHEMA, FEEDBACK_TABLE_SCHEMA, SOURCES_TABLE_SCHEMA

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
        # create tables if they do not exist
        for schema in [PROBLEMS_TABLE_SCHEMA, SOLUTIONS_TABLE_SCHEMA, ATTEMPTS_TABLE_SCHEMA, FEEDBACK_TABLE_SCHEMA, SOURCES_TABLE_SCHEMA]:
            cursor.execute(schema)
        
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
    # This function can be expanded to include more sample data as needed.
    LEETCODE_PROBLEMS = [
        ("Climbing Stairs", "You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?", "Easy", "dynamic programming, recursion", "LeetCode"),
        ("Two Sum", "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.", "Easy", "array, hash table", "LeetCode"),
        ("Unique Paths", "A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below). The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below). How many possible unique paths are there?", "Medium", "dynamic programming, combinatorics", "LeetCode"),
        ("Longest Substring Without Repeating Characters", "Given a string s, find the length of the longest substring without repeating characters.", "Medium", "hash table, sliding window", "LeetCode"),
        ("Merge Intervals", "Given a collection of intervals, merge all overlapping intervals. For example, given intervals [1,3],[2,6],[8,10],[15,18], return [1,6],[8,10],[15,18].", "Medium", "array, sorting", "LeetCode"),
        ("Course Schedule", "There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]. Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?", "Medium", "graph, topological sort", "LeetCode"),
        ("Alien Dictionary", "Given a list of words from the alien language, find the order of characters in the alien language. The input is a list of words sorted lexicographically by the rules of the alien language.", "Hard", "graph, topological sort", "LeetCode"),
    ]

    QUANT_PROBLEMS = [
        ("Chapter 1 Problem 15", "A stock with spot price $40 pays dividends continuously at a rate of 3%. The 4 months at-the-money put and call options on this asset are trading at $2 and $4 respectively. The risk free rate is constant and equal to 5%. Show that the Put-Call parity is not satisfied and explain how would you take advantage of this arbitrage opportunity", "Hard", "arbitrage, options pricing", "A Primer on Quantitative Finance"),
        ("Question 7", "Suppose you have in your possession an incredibly large bag of M&Ms containing a uniform distribution of the six M&M colors. You decide to play a game: you draw one M&M from the bag and place it on the table. You then continue to draw M&M's from the bag one at a time. If you draw an M&M that is the same color as one already on the table, you eat both of them. Other wise, you place the M&M on the table along with the others of different color. The game ends when you have six M&M's on the table. How many M&M's should you expect to eat playing this game? ", "Hard", "probability, expectation, first-step-analysis, markov-chains", "150 Most Common Quantitative Finance Interview Questions"),
        ("Face-to-face Question", "Roll two dice. What is the probability that one is larger than the other?", "probability-basic, axioms-of-prob", "Quantitative Primer"),
        ("Phone Interview", "You are presented with the following gamble: you flip 100 fair coins. If 60 or more land on heads, you win £10; you win nothing on all other outcomes. Should you play this game for £1?", "conditinoal-prob, probability, expectation", "Quantitative Primer"),
        ("Stick Breaking Problem", "Break a 1m stick in two random places. What is the probability that the three resulting pieces orm a triangle?", "conditional-prob, probability", "Quantitative Primer")
    ]

    SOURCES = [
        ("LeetCode", "SWE", "https://leetcode.com", None),
        ("Green Book", "Quant", None, "Quant interview Prep Book"),
       ("Harvard 110 Text Book", "Quant", None, "Intro to Probability"),
       ("Green Book", "Quant", None, "Intro to Probability"), 
    ]
