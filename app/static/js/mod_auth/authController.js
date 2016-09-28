app.controller("loginCtrl", function($scope, $location, ajaxCallService) {
	
	$scope.message= false;
	
	$scope.validateUser = function(loginData) {
		ajaxCallService.postData("/api/login", loginData)
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


app.controller("signupCtrl", function($scope, $location, ajaxCallService) {
	$scope.createUser = function(signupData) {
		
		ajaxCallService.postData("/api/signup", signupData)
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

