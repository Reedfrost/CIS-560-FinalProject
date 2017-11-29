import psycopg2
import sys

class Query():
    def __init__(self):
        super().__init__()
        conn_string = "host='postgresql.cs.ksu.edu' port=5432 dbname='badonmap' user='badonmap' password=''"
        try:
            self.conn = psycopg2.connect(conn_string)
            self.cursor = self.conn.cursor()
            print("pass")
        except:
            print("fail")
    
    #A function to validate a student ID's existance
    def validateName(self, name):
        query = "SELECT name FROM students WHERE id={}".format(name)
        try:
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            print(data[0])
            self.cursor.commit()
            return True
        except:
            print("This student doesn't exist")
            return False
    
    #A function to validate a strike ID's existance
    def validateStrike(self, id):
        query = "SELECT name FROM writeUps WHERE id={}".format(id)
        try:
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            print(data[0])
            self.conn.commit()
            return True
        except:
            print("That strike doesn't exist")
            return False
    
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
            self.conn.commit()
        except:
            print("fail")
        
    def newStudent(self, name):
        query = "INSERT INTO students VALUES(DEFAULT, '{}')".format(name)
        self.cursor.execute(query)
        self.conn.commit()
        
    def newStrike(self, description, strike):
        query = "INSERT INTO writeups VALUES(DEFAULT, '{}', '{}')".format(strike, description)
        self.cursor.execute(query)
        self.conn.commit()
        
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
        for d in data:
            s=""
            for l in d:
                s += '{}'.format(l) + ' '
            print(s + '\n')
        
    def fired(self, sid):
        query = "DELETE FROM students WHERE id={}".format(sid)
        self.cursor.execute(query)
        self.conn.commit()
        
    def schedule(self):
        query = "SELECT s.name as student, d.name as day, to_char(w.strt, 'HH12:MI:SS AM') as start, to_char(w.fnsh, 'HH12:MI:SS AM') as finish, a.name as area, j.name as job \n" + \
                "FROM works w \n" + \
                "JOIN students s ON w.sid = s.id \n" + \
                "JOIN days d ON w.did = d.id \n" + \
                "JOIN areas a ON w.aid = a.id \n" + \
                "JOIN jobs j ON w.jid = j.id \n" + \
                "ORDER BY w.did, w.strt;"
        self.printQuery(query)
            
    def close(self):
        print("Closing connection")
        self.cursor.close()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
