var app = angular.module("myApp", ["ngRoute"]);

app.config(function($routeProvider) {
	$routeProvider
		.when("/about", {
			templateUrl : "/static/partials/about.html",
			controller : ""
		})
		.when("/contact", {
			templateUrl : "/static/partials/contact.html",
			controller : ""
		})
		.when("/404", {
			templateUrl : "/static/partials/404.html",
			controller : ""
		})
		.when("/login", {
			templateUrl : "/static/partials/mod_auth/login.html",
			controller : "loginCtrl"
		})
		.when("/home", {
			templateUrl : "/static/partials/mod_users/user_home.html",
			controller : "userhomeCtrl"
		})
		.when("/signup", {
			templateUrl : "/static/partials/mod_users/signup.html",
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
		.when("/latest_news", {
			templateUrl : "/static/partials/mod_posts/latest_news.html",
			controller : "latestNewsCtrl"
		})
		.otherwise({
		redirectTo : "/home"
	});
});


/* Global Services */
app.service("ajaxCallService", function($http) {
	
	this.getData = function(url) {
		return $http.get(url);
	}
	
	this.postData = function(url, data) {
		return $http.post(url, data);
	}
});

app.service("checkNumberService", function() {
	
	this.isInt = function(value) {
		 if (isNaN(value)) {
			 return false;
		 }
		 
		 var x = parseInt(value);
		 if(x == value) {
			 return true;
		 }
		 else {
			 return false;
		 }
	}
});

