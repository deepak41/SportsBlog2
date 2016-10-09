'''
Created on Sep 13, 2016

@author: Deepak
'''
from app.bloglib.dbConfig import db_connect

class UserModel(object):


    def __init__(self):
        self.conn = db_connect()
        self.cursor = self.conn.cursor()
    
    
    def createUser(self, signupData):
        firstname = signupData.get("firstname")
        lastname = signupData.get("lastname")
        email = signupData.get("email")
        password = signupData.get("password")
        
        stmt_insert = "INSERT INTO users (firstname, lastname, email, pwdhash) VALUES (%s, %s, %s, %s);"
        values = [firstname, lastname, email, password]
        
        self.cursor.execute(stmt_insert, values)
        self.conn.commit()
        
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
        
        
    
    def getByEmail(self, email):
        stmt_select = "select * from users where BINARY email = %s;"
        values = [email]
        
        self.cursor.execute(stmt_select, values)
        row = self.cursor.fetchone()
        
        return row
    
    
    
    