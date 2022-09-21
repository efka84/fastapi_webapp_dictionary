import sqlite3 as SQL

def match_exact(word:str)->list:
    """
    this method will 
    1. accept a string
    2. search the dictionary for an exact match
    3. if success returns the found word else an empty list 
    """
    # establish connection to dictinoary.db

    db = SQL.connect("data/dictionary.db")

    # query the database for exact matches
    sql_query ="SELECT * from entries WHERE word=?"
    match = db.execute(sql_query, (word,)).fetchall()

    #close the connection to database
    db.close()

    return match  


def match_like (word: str) -> list: 
   """ 
   This method will: 
   1. Accept a string 
   2. Search the dictionary for approximate matches 
   3. If success return the definition as a list 
   4. If not return an empty list 
   """ 
   # Establish connection to the dictionary database 
   db = SQL.connect( "data/dictionary.db" ) 

   # Query the database for exact matches 
   sql_query = "SELECT * from entries WHERE word LIKE ?" 
   match = db.execute(sql_query, ( "%" + word + "%" ,)).fetchall() 

   # Clone the connection to the database 
   db.close() 
   # Return the results 
   return match
