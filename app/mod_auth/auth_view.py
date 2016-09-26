import json

from flask import Flask, render_template
from flask import request
from flask.globals import session
from flask.views import MethodView

from app.bloglib.dbConfig import db_connect


class AuthView(MethodView):
    def get(self):
        return
    
    def post(self):
        pass
    

class LoginView(MethodView):
    def post(self):
        loginData = json.loads(request.data)
        
        email = loginData.get("email")
        password = loginData.get("password")
        
        cnx = db_connect()
        cur = cnx.cursor()
        
        stmt_select = "select uid, firstname, pwdhash from users where email = %s;"
        values = [email]
        
        cur.execute(stmt_select, values)
        row = cur.fetchone()
        
        if row:
            data = {
                "uid":row[0],
                "firstname":row[1],
                "pwdhash":row[2],
            }
            
            if password == data["pwdhash"]:
                session["userId"] = data["uid"]
                session["firstname"] = data["firstname"]
                return "Login Successful"
            else:
                return "Login Unsuccessful"
        else:
            return "Login Unsuccessful"

    
class SignupView(MethodView):
    def post(self):
        print "****** Rainy Day **********"
        signupData = json.loads(request.data)
        
        firstname = signupData.get("firstname")
        lastname = signupData.get("lastname")
        email = signupData.get("email")
        password = signupData.get("password")
        
        cnx = db_connect()
        cur = cnx.cursor()
        
        stmt_insert = "INSERT INTO users (firstname, lastname, email, pwdhash) VALUES (%s, %s, %s, %s);"
        values = [firstname, lastname, email, password]
        
        cur.execute(stmt_insert, values)
        cnx.commit()
        
        return "Signup Successful"
        