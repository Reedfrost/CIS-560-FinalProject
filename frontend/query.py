import psycopg2
import sys

class Query():
    def __init__(self):
        super().__init__()
        conn_string = "host='postgresql.cs.ksu.edu' port=5432 dbname='badonmap' user='badonmap' password=''"
        try:
            conn = psycopg2.connect(conn_string)
            self.cursor = conn.cursor()
            print("pass")
        except:
            print("fail")
    
    #A function to validate a student ID's existance
    def validateName(self, name):
        query = "SELECT name FROM students WHERE id={}".format(name)
        try:
            self.cursor.execute(query)
            return true
        except:
            print("This student doesn't exist")
            return false
    
    #A function to validate a strike ID's existance
    def validateStrike(self, id):
        query = "SELECT name FROM writeUps WHERE id={}".formate(id)
        try:
            self.cursor.execture(query)
            return true
        except:
            print("That strike doesn't exist")
            return false
    
    def searchQuery(self, name):
        if name == 'all':
            query = "SELECT * FROM students"
            self.printQuery(query)
        else:
            query = "SELECT name FROM students WHERE id={}".format(name)
            try:
                self.printQuery(query)
                return True
            except:
                print("This student doesn't exist {}".format(name))
                return False
    def strike(self, mid, sid, wid, day, month, year):
        try:
            query = "INSERT INTO occurs VALUES({}, {}, {}, to_date('{} {} {}', 'DD Mon YYYY'))".format(mid, sid, wid, day, month, year)
            self.cursor.execute(query)
        except:
            print("fail")
        
    def newStudent(self, name):
        query = "INSERT INTO students VALUES(DEFAULT, '{}')".format(name)
        self.cursor.execute(query)
        
    def newStrike(self, description, strike):
        query = "INSERT INTO writeups VALUES(DEFAULT, '{}', '{}')".format(strike, description)
        self.cursor.execute(query)
        
    def kramer_login(self, username, password):
        query = "SELECT id FROM managers WHERE username='{}' AND password='{}'".format(username, password)
        print(query)
        try:
            self.cursor.execute(query)
            print("YOU IN")
            data = self.cursor.fetchall()
            return data[0]
        except:
            print("Fail")
            return -1
            
    def viewStrikes(self):
        query = "SELECT * FROM writeups"
        self.printQuery(query)
        
    def list_offenders(self):
        query = "SELECT * FROM offenders"
        self.printQuery(query)
        
    def printQuery(self, query):
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        print(data)
        
    def fired(self, sid):
        query = "DELETE FROM students WHERE id={}".format(sid)
            
    def close(self):
        print("Closing connection")
        self.cursor.close()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
