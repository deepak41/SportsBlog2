from flask import Flask

from app.mod_auth.auth_view import AuthView
from app.mod_index.IndexView import IndexView
from app.mod_auth.auth_view import LoginView, SignupView
from app.mod_posts.PostsView import PostsView, CreatePostView
from app.mod_users.UserView import UserHomeView


app = Flask(__name__, template_folder="app/templates", static_folder="app/static")
app.secret_key = "development key"


authApi = AuthView.as_view('user_view')
indexApi = IndexView.as_view('index_view')
loginView = LoginView.as_view("login_view")
signupView = SignupView.as_view("signup_view")
userHomeView = UserHomeView.as_view("userHome_view")
postsView = PostsView.as_view("posts_view")
createPostView = CreatePostView.as_view("CreatePostView")


app.add_url_rule('/', view_func=indexApi, methods=['GET'])
app.add_url_rule('/api/login', view_func=loginView, methods=['POST'])
app.add_url_rule('/api/signup', view_func=signupView, methods=['POST'])
app.add_url_rule('/api/userhome', view_func=userHomeView, methods=['GET'])
app.add_url_rule('/api/post/<postId>', view_func=postsView, methods=['GET'])
app.add_url_rule('/api/createpost', view_func=createPostView, methods=['POST'])


if __name__ == "__main__":
    app.run(debug=True)