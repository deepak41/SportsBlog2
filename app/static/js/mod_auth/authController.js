app.service("postService", function($http) {
	
	this.postData = function(url, data) {
		return $http.post(url, data);
	}
});


app.controller("loginCtrl", function($scope, $location, postService) {
	
	$scope.message= false;
	
	$scope.validateUser = function(loginData) {
		postService.postData("/logging", loginData)
			.success(function(response) {
				console.log(response);
				
				if(response == "Login Successful") {
					$location.path("/home");
				}
				else {
					console.log("********* MM");
					$scope.message= true;
				}
			})
		    .error(function(err){
		    	
		    });
	}
});


app.controller("signupCtrl", function($scope, $location, postService) {
	$scope.createUser = function(signupData) {
		
		postService.postData("/signupp", signupData)
			.success(function (response) {
				console.log(response);
				
				if(response == "Signup Successful") {
					$location.path("/home");
				}
				else {
					console.log("********* MM");
				}
			})
		    .error(function(err){
		    	
		    });
	}
	
});

