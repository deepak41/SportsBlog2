import time

from flask.globals import session

from app.bloglib.dbConfig import db_connect


class PostsModel(object):
    
    def __init__(self):
        self.conn = db_connect()
        self.cursor = self.conn.cursor()
        
    
    def getLatestPosts(self, skipRows, noOfRows):
        stmt_select = "SELECT * FROM posts ORDER BY pid DESC LIMIT %s, %s;"
        
        stmt_select2 = "SELECT posts.*, users.firstname, users.lastname FROM users inner join posts on users.uid = posts.uid ORDER BY pid DESC LIMIT %s, %s;"
        
        values = [skipRows, noOfRows]
        
        self.cursor.execute(stmt_select2, values)
        
        records = self.cursor.fetchall()
        
        return records
        
    
    def getLatestPostsByRegion(self, skipRows, noOfRows, region):
        
        stmt_select = "SELECT posts.*, users.firstname, users.lastname FROM users inner join posts on users.uid = posts.uid where region = %s ORDER BY pid DESC LIMIT %s, %s;"
        values = [region, skipRows, noOfRows]
        
        self.cursor.execute(stmt_select, values)
        
        records = self.cursor.fetchall()
        
        return records
    
    
    def getPostById(self, postId):
        stmt_select = "SELECT posts.*, users.firstname, users.lastname FROM users inner join posts on users.uid = posts.uid where pid = %s;"
        values = [postId]
        self.cursor.execute(stmt_select, values)
        
        row = self.cursor.fetchone()
        
        print row
        return row
    
    
    def createPost(self, formData):
        subject = formData.get("subject")
        post_content = formData.get("post_content")
        region = formData.get("region")
        
        
        stmt_insert = "INSERT INTO posts (uid, subject, post_content, region, date) VALUES (%s, %s, %s, %s, %s)"
        values = [session["userId"], subject, post_content, region, int(time.time())]

        self.cursor.execute(stmt_insert, values)
        self.conn.commit()
        
        return "success"
    
    
    def editPost(self, postId, formData):
        subject = formData.get("subject")
        post_content = formData.get("post_content")
        region = formData.get("region")
        last_update_date = int(time.time())
        
        
        stmt_insert = "UPDATE posts SET subject=%s, post_content=%s, region=%s, last_update_date=%s WHERE pid=%s;"
        values = [subject, post_content, region, last_update_date, postId]
        
        # try catch block here
        self.cursor.execute(stmt_insert, values)
        self.conn.commit()
        
        return "success"
        
        
        
        
        
        
        
        
        