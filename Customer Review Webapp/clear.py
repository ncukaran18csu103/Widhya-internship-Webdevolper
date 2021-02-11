import sqlite3

con = sqlite3.connect("reviews.db")
cur = con.cursor()
cur.execute("DROP TABLE REVIEWS")