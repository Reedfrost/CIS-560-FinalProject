import psycopg2
import sys

class connector():
    hostname = 'psql.cs.ksu.edu'
    port = 5432
    username = 'badonmap'
    password = ''
    database = 'badonmap'
    myConnection = pgdb.connect(host=hostname, user=username, password=password, datbase=database)