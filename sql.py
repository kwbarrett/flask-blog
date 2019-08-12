# sql.py Create a sqlite3 table and populate it with data

import sqlite3

# create new database if it doesn't already exist
with sqlite3.connect("blog.db") as connection:

    # get a cursor object used to execute SQL
    cursor = connection.cursor()

    # create the posts table
    cursor.execute("""CREATE TABLE posts
                    (title TEXT, post TEXT)
                    """)

    # insert dummy data in the table
    cursor.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
    cursor.execute('INSERT INTO posts VALUES("Well", "I\'m well.")')
    cursor.execute('INSERT INTO posts VALUES("Excellent", "I\'m excellent.")')
    cursor.execute('INSERT INTO posts VALUES("Okay", "I\'m okay.")')

