import time

from flask.globals import session

from app.bloglib.dbConfig import db_connect


class PostsModel(object):
    
    def __init__(self):
        self.conn = db_connect()
        self.cursor = self.conn.cursor()
        
    
    def getLatestPosts(self, skipRows, noOfRows):
        stmt_select = "SELECT * FROM posts ORDER BY pid DESC LIMIT %s, %s;"
        values = [skipRows, noOfRows]
        
        self.cursor.execute(stmt_select, values)
        
        records = self.cursor.fetchall()
        
        return records
        
    
    def getLatestPostsByRegion(self, skipRows, noOfRows, region):
        
        stmt_select = "SELECT * FROM posts where region = %s ORDER BY pid DESC LIMIT %s, %s;"
        values = [region, skipRows, noOfRows]
        
        self.cursor.execute(stmt_select, values)
        
        records = self.cursor.fetchall()
        
        return records
    
    
    def getPostById(self, postId):
        
        stmt_select = "select * from posts where pid = %s;"
        values = [postId]
        
        self.cursor.execute(stmt_select, values)
        
        row = self.cursor.fetchone()
        
        return row
    
    
    def createPost(self, formData):
        subject = formData.get("subject")
        post_content = formData.get("post_content")
        
        
        stmt_insert = "INSERT INTO posts (uid, subject, post_content, region, date) VALUES (%s, %s, %s, %s, %s)"
        values = [session["userId"], subject, post_content, "ASIA", int(time.time())]

        self.cursor.execute(stmt_insert, values)
        self.conn.commit()
        
        return "success"
        
        
        
        
        
        
        
        
        