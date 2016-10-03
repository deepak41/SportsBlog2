from flask import render_template
from flask.globals import session
from flask.views import MethodView


class IndexView(MethodView):
    def get(self):
        userId = session.get("userId")
        firstname = session.get("firstname")
        
        sessioninfo = {"userId":userId, "firstname":firstname}
        
        return render_template("index.html", sessioninfo=sessioninfo )
       

    def post(self):
        pass