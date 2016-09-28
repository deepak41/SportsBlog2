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
    
    
        
        
        