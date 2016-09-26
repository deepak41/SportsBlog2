from flask import Flask, render_template
from flask.views import MethodView

class IndexView(MethodView):
    def get(self):
        return render_template("layout.html")
    
    def post(self):
        pass