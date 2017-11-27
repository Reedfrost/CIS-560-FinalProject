import psycopg2
import sys
from dbconn.py import connector

class assign:
    connection = connector.myConnection.cursor()
    def searchQuery(id, level):
        if name == 'all':
	        query = "SELECT * FROM student"
            #connection.execute(query)
        else:
            query = "SELECT {} FROM student".format(id)
            try:
                connection.execute(query)
            except:
                print("This student doesn't exist {}".format(id))
    def strike(student, strike):
        query = "INSERT INTO writeUps VALUES"
        connection.execute(query)
    def newStudent(name):
        query = "INSERT INTO students VALUES(1, {})".format(name)
    def newStrike(description, strike):
        query = "INSERT INTO writeUps VALUES(1, {}, {}, ?)".format(strike, description)
    def close():
	    connector.myConnection.close()