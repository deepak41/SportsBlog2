from datetime import datetime
import json
from flask import request
from flask.views import MethodView

from app.mod_posts.PostsModel import PostsModel


class PostsView(MethodView):
    
    def get(self, postId):
        postsModel = PostsModel()
        
        output = []
        
        row = postsModel.getPostById(postId)
        
        t = datetime.fromtimestamp(row[5])
            
        data = {
            "pid":row[0],
            "uid":row[1],
            "subject":row[2],
            "post_content":row[3],
            "region":row[4],
            "date":t.strftime("%d-%b-%Y %H:%M"),
            "author": row[6]+" "+row[7]
        }
        
        output.append(data)
        
        return json.dumps(output)
    
    
class CreatePostView(MethodView):
    def post(self):
        
        formData = json.loads(request.data)
        postsModel = PostsModel()
        
        result = postsModel.createPost(formData)
        
        return result
    
    
class LatestNewsView(MethodView):
    def get(self):
        page = request.args.get("page", 1)
        
        try:
            page = int(page)
        except:
            pass
        
        skipRows = 5*(page-1)
        
        postsModel = PostsModel()
        output = []
        
        records = postsModel.getLatestPosts(skipRows, 5)
        
        for row in records:
            t = datetime.fromtimestamp(row[5])
            post_content = row[3][0:270] + "..."
            subject = row[2]
            
            if len(subject) > 100:
                subject = row[2][0:120] + "..."
            
            data = {
                "pid": row[0],
                "uid": row[1],
                "subject": subject,
                "post_content": post_content,
                "region": row[4],
                "date": t.strftime("%d-%b-%Y %H:%M"),
                "author": row[6]+" "+row[7]
            }
            output.append(data)
            
        return json.dumps(output)
        
        
        
    
    
        
        
        