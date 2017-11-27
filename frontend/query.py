import psycopg2
import sys
from dbconn.py import connector

class assign:
    def searchQuery(id, level):
        connection = connector.myConnection.cursor()
        if name == 'all':
	        query = "SELECT * FROM student"
            #connection.execute(query)
        else:
            query = "SELECT {} FROM student".format(id)
            try:
                connection.execute(query)
            except:
                print("This student doesn't exist {}".format(id))
    def close():
	    connector.myConnection.close()