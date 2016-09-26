'''
Created on Sep 13, 2016

@author: Deepak
'''
from app.bloglib.dbConfig import db_connect

class UserModel(object):


    def __init__(self, params):
        self.conn = db_connect()
        self.cursor = self.conn.cursor()
        
    def create(self, name, email, password):
        stmt_insert = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
        values = []
        self.cursor.execute(stmt_insert, values)
        self.cursor.commit()
        
        return 
    
    def get(self, user_id):
        stmt_select = "select * from users where user_id=%s;"
        values = [user_id]
        self.cursor.execute(stmt_select, values)
        row = self.cursor.fetchone()
        
        return row
    
    def remove(self, user_id):
        st = "delete from users where user_id = %s"
        values = [user_id]
        self.cursor.execute(st, values)
        
        
        
    