import cx_Oracle as pyo
from oracle_config import dbcon

class Bookdb:
    con = pyo.connect(dbcon)
    cursor = con.cursor()

    def __init__(self) -> None:        
        self.con = pyo.connect(dbcon)
        self.cursor = self.con.cursor()
        print("You have connected to the database")
    
    def __del__(self):
        self.con.close()

    def view(self):
        self.cursor.execute("SELECT * FROM BOOKS")                
        rows = self.cursor.fetchall()
        print(rows)
        return rows

    def insert(self,title,author,isbn):
        sql=("INSERT INTO books(title,author,isbn) VALUES (:title,:author,:isbn)")
        values = [title,author,isbn]
        query = self.cursor.execute(sql,values)
        self.con.commit()
        return "New book added to database"

    def update(self, id, title, author, isbn):
        tsql = 'UPDATE books SET title = :title, author=:title, isbn=:isbn WHERE id=:id'
        self.cursor.execute(tsql, [title,author,isbn,id])
        self.con.commit()
        return "New book added to database"

    def delete(self, id):
        delquery = 'DELETE FROM books WHERE id = :id'
        self.cursor.execute(delquery, [id])
        self.con.commit()
        return "Book deleted"
