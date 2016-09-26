from datetime import datetime
import json

from flask import request
from flask.views import MethodView

from app.mod_posts.PostsModel import PostsModel
from app.mod_users.UserModel import UserModel


class UserHomeView(MethodView):
    
    def get(self):
        postsModel = PostsModel()
        output = {"section1":[], "section2":[]}
        
        # section 1
        records = postsModel.getLatestPosts(0, 3)
        
        for row in records:
            t = datetime.fromtimestamp(row[5])
            post_content = row[3][0:140]
            
            data = {
                "pid":row[0],
                "uid":row[1],
                "subject":row[2],
                "post_content":post_content,
                "region":row[4],
                "date":t.strftime("%d-%b-%Y %H:%M"),
            }
            output["section1"].append(data)
            
            
        # section 2
        regions = ["ASIA", "AFRICA", "EUROPE", "SOUTH AMERICA"]
        
        for region in regions:
            row = postsModel.getLatestPostsByRegion(0, 1, region)
            
            t = datetime.fromtimestamp(row[0][5])
            post_content = row[0][3][0:200]
             
            data = {
                "pid":row[0][0],
                "uid":row[0][1],
                "subject":row[0][2],
                "post_content":post_content,
                "region":row[0][4],
                "date":t.strftime("%d-%b-%Y %H:%M"),
            }
            output["section2"].append(data)

        return json.dumps(output)
        