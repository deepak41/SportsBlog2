import json

from flask import Flask, render_template
from flask import request
from flask.globals import session
from flask.views import MethodView
from werkzeug import redirect

from app.bloglib.dbConfig import db_connect
from app.mod_users.UserModel import UserModel


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
        
        response = {"status":"", "message":"", "data":""}
        
        userModel = UserModel()
        row = userModel.getByEmail(email)
        
        if row:
            data = {
                "uid":row[0],
                "firstname":row[1],
                "pwdhash":row[4],
            }
            
            if password == data["pwdhash"]:
                session["userId"] = data["uid"]
                session["firstname"] = data["firstname"]
                
                response["status"] = "SUCCESS"
                response["message"] = "Login Successful!"
                response["data"] = None
            else:
                response["status"] = "ERROR"
                response["message"] = "Either email or password is invalid!"
                response["data"] = None
        else:
            response["status"] = "ERROR"
            response["message"] = "Either email or password is invalid!"
            response["data"] = None
        
        return json.dumps(response)
        

class LogoutView(MethodView):
    def get(self):
        del session["userId"]
        del session["firstname"]
        return redirect("/")
        