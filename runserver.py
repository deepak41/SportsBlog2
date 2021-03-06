from flask import Flask

from app.mod_auth.auth_view import AuthView, LogoutView
from app.mod_auth.auth_view import LoginView
from app.mod_index.IndexView import IndexView
from app.mod_posts.PostsView import PostsView, CreatePostView, LatestNewsView, EditPostView
from app.mod_users.UserView import UserHomeView, SignupView


app = Flask(__name__, template_folder="app/templates", static_folder="app/static")
app.secret_key = "development key"


authApi = AuthView.as_view('user_view')
logoutApi = LogoutView.as_view('logout_view')
indexApi = IndexView.as_view('index_view')
loginView = LoginView.as_view("login_view")
signupView = SignupView.as_view("signup_view")
userHomeView = UserHomeView.as_view("userHome_view")
postsView = PostsView.as_view("posts_view")
createPostView = CreatePostView.as_view("createPost_View")
editPostView = EditPostView.as_view("editPost_View")
latestNewsView = LatestNewsView.as_view("latestNews_View")


app.add_url_rule('/', view_func=indexApi, methods=['GET'])
app.add_url_rule('/logout', view_func=logoutApi, methods=['GET'])
app.add_url_rule('/api/login', view_func=loginView, methods=['POST'])
app.add_url_rule('/api/signup', view_func=signupView, methods=['POST'])
app.add_url_rule('/api/userhome', view_func=userHomeView, methods=['GET'])
app.add_url_rule('/api/post/<postId>', view_func=postsView, methods=['GET'])
app.add_url_rule('/api/createpost', view_func=createPostView, methods=['POST'])
app.add_url_rule('/api/editpost/<postId>', view_func=editPostView, methods=['POST'])
app.add_url_rule('/api/get_latestposts', view_func=latestNewsView, methods=['GET'])
app.add_url_rule('/api/get_latestposts/<area>', view_func=latestNewsView, methods=['GET'])
app.add_url_rule('/api/get_latestposts/<area>/<region>', view_func=latestNewsView, methods=['GET'])


if __name__ == "__main__":
    app.run(debug=True)