app.controller("loginCtrl", function($scope, $location, $window, ajaxCallService) {
	
	var message = {"status":"success", "title":"SUCCESS","content":"Login Successful!"};
	
	$scope.validateUser = function(loginData) {
		ajaxCallService.postData("/api/login", loginData)
			.success(function(response) {
				console.log(response);
				
				if(response == "Login Successful") {
					$location.path("/home");
					$window.location.reload();
				}
				else {
					console.log("********* MM");
					
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

