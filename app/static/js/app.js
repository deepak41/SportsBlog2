var app = angular.module("myApp", ["ngRoute"]);

app.config(function($routeProvider) {
	$routeProvider
		.when("/login", {
			templateUrl : "/static/partials/login.html",
			controller : "loginCtrl"
		})
		.when("/home", {
			templateUrl : "/static/partials/mod_users/user_home.html",
			controller : "userhomeCtrl"
		})
		.when("/signup", {
			templateUrl : "/static/partials/mod_auth/signup.html",
			controller : "signupCtrl"
		})
		.when("/post/:postid", {
			templateUrl : "/static/partials/mod_posts/post.html",
			controller : "viewPostCtrl"
		})
		.when("/write_post", {
			templateUrl : "/static/partials/mod_posts/write_post.html",
			controller : "writePostCtrl"
		})
		.when("/edit_post", {
			templateUrl : "/static/partials/mod_posts/edit_post.html",
			controller : "editPostCtrl"
		})
		.otherwise({
		redirectTo : "/login"
		
	});
		
});