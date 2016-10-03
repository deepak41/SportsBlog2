from datetime import datetime
import json

from flask import request
from flask.views import MethodView
from werkzeug.exceptions import abort

from app.mod_posts.PostsModel import PostsModel


class PostsView(MethodView):
    
    def get(self, postId):
        postsModel = PostsModel()
        output = []
        
        response = {"status":"", "message":"", "data":""}
        
        try:
            postId = int(postId)
        except:
            abort(404)
        
        row = postsModel.getPostById(postId)
        
        creationDate = row[5]
        updationDate = row[6]
        t = datetime.fromtimestamp(updationDate if updationDate else creationDate)
        
        data = {
            "pid":row[0],
            "uid":row[1],
            "subject":row[2],
            "post_content":row[3],
            "region":row[4],
            "date":t.strftime("%d-%b-%Y %H:%M"),
            "author": row[7]+" "+row[8]
        }
        
        output.append(data)
        
        response["status"] = "SUCCESS"
        response["message"] = "Post found successfully!"
        response["data"] = output
        
        return json.dumps(response)
    
    
class CreatePostView(MethodView):
    def post(self):
        
        formData = json.loads(request.data)
        
        response = {"status":"", "message":"", "data":""}
        
        postsModel = PostsModel()
        
        result = postsModel.createPost(formData)
        
        response["status"] = "SUCCESS"
        response["message"] = "Post created successfully!"
        response["data"] = None
        
        return json.dumps(response)
    
    
class EditPostView(MethodView):
    def post(self, postId):
        
        formData = json.loads(request.data)
        
        response = {"status":"", "message":"", "data":""}
        
        postsModel = PostsModel()
        
        result = postsModel.editPost(postId, formData)
        
        response["status"] = "SUCCESS"
        response["message"] = "Post updated successfully!"
        response["data"] = None
        
        return json.dumps(response)
    
    
class LatestNewsView(MethodView):
    def get(self, area=None, region=None):
        
        response = {"status":"", "message":"", "data":""}
        
        page = request.args.get("page", 1)
        
        try:
            page = int(page)
        except:
            pass
        
        skipRows = 5*(page-1)
        
        postsModel = PostsModel()
        output = []
        records = []
        

        if (area in ["all", None]) and region==None:
            records = postsModel.getLatestPosts(skipRows, 5)
        
        elif area == "area" and region != None:
            records = postsModel.getLatestPostsByRegion(skipRows, 5, region)
        
        for row in records:
            post_content = row[3][0:270] + "..."
            subject = row[2]
            
            if len(subject) > 100:
                subject = row[2][0:120] + "..."
                
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
            output.append(data)
            
            response["status"] = "SUCCESS"
            response["message"] = "Posts found successfully!"
            response["data"] = output
        
        return json.dumps(response)
