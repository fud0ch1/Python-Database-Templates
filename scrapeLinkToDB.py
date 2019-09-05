import sqlite3


class Database:

    # Connect Function causes the frontend to connect with sqlite3 db
    # and establish a table if one doesnt exist
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS articledb (id INTEGER PRIMARY KEY, articleUrl text, articleTitle text, articleAuthor text, articleContent text, articleDate text)")
        self.conn.commit()

    # The Insert Function will insert a 'book' into the sqlite3 db
    # The book has '5' values, NULL assigns a random numberic id value;
    # the rest are title author year and isbn
    def insert(self, articleUrl, articleTitle, articleAuthor, articleContent, articleDate):
        # NULL is to pass the random 'id' INTEGER PRIMARY KEY
        self.cur.execute("INSERT INTO articledb VALUES (NULL, ?, ?, ?, ?, ?)", (articleUrl, articleTitle, articleAuthor, articleContent, articleDate))
        self.conn.commit()

    # The View Function will show all entries for every 'book' in the sqlite3db
    def view(self):
        self.cur.execute("SELECT * FROM articledb")
        rows = self.cur.fetchall()
        return rows

    # The Search function will search for only one or all of the variables
    # Variables are followed by 'var = ""' to avoid passing errors
    # In the case for when you leave an entry window blank
    def search(self, articleUrl='', articleTitle="", articleAuthor="", articleContent="", articleDate=""):
        self.cur.execute("SELECT * FROM articledb WHERE articleUrl = ? OR articleTitle = ? OR articleAuthor = ? OR articleContent = ? OR articleDate = ?", (articleUrl, articleTitle, articleAuthor, articleContent, articleDate))
        rows = self.cur.fetchall()
        return rows

    # The Delete Function must 'grab' the 'id' of a book to delete it
    def delete(self, id):
        self.cur.execute("DELETE FROM articledb WHERE id = ?", (id,))
        self.conn.commit()

    # Update information on a book
    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE articledb SET articleUrl = ?, articleTitle = ?, author = ?, year = ?, isbn=? WHERE id = ?",(title, author, year, isbn, id))
        self.conn.commit()

    # Ends database connection
    def __del__(self):
        self.conn.close
