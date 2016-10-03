from datetime import datetime
import json

from flask import request
from flask.views import MethodView

from app.mod_posts.PostsModel import PostsModel
from app.mod_users.UserModel import UserModel


class UserHomeView(MethodView):
    
    def get(self):
        response = {"status":"", "message":"", "data":""}
        
        postsModel = PostsModel()
        output = {"section1":[], "section2":[]}
        
        # section 1 (Latest News block)
        records = postsModel.getLatestPosts(0, 3)
        
        for row in records:
            post_content = row[3][0:170] + "..."
            subject = row[2]
            
            if len(subject) > 65:
                subject = row[2][0:65] + "..."
                
            creationDate = row[5]
            updationDate = row[6]
            t = datetime.fromtimestamp(updationDate if updationDate else creationDate)
            
            data = {
                "pid": row[0],
                "uid": row[1],
                "subject": subject,
                "post_content": post_content,
                "region": row[4],
                "date": t.strftime("%d-%b-%Y %H:%M"),
                "author": row[7]+" "+row[8]
            }
            output["section1"].append(data)
            
            
        # section 2
        regions = ["europe", "asia", "africa", "southamerica"]
        
        for region in regions:
            row = postsModel.getLatestPostsByRegion(0, 1, region)
            
            post_content = row[0][3][0:200] + "..."
            subject = row[0][2]
            
            if len(subject) > 100:
                subject = row[0][2][0:100] + "..."
                
            creationDate = row[0][5]
            updationDate = row[0][6]
            t = datetime.fromtimestamp(updationDate if updationDate else creationDate)
             
            data = {
                "pid":row[0][0],
                "uid":row[0][1],
                "subject":subject,
                "post_content":post_content,
                "region":row[0][4],
                "date":t.strftime("%d-%b-%Y %H:%M"),
                "author": row[0][7]+" "+row[0][8]
            }
            output["section2"].append(data)

        response["status"] = "SUCCESS"
        response["message"] = "Data found successfully!"
        response["data"] = output
        
        return json.dumps(response)

        