app.controller("loginCtrl", function($scope, $location, $window, ajaxCallService, toasterService) {
	
	var message = {"status":"", "title":"","content":""};
	
	$scope.validateUser = function(loginData) {
		ajaxCallService.postData("/api/login", loginData)
			.success(function(response) {
				
				if(response.status == "SUCCESS") {
					$window.location.reload();
					$location.path("/home");
				}
				else {
					message.status="error";
					message.title=response.status;
					message.content=response.message;
					
					toasterService.popMessage(message);
				}
			})
		    .error(function(err){
		    	
		    });
	}
});


app.controller("signupCtrl", function($scope, $location, ajaxCallService, toasterService) {
	
	var message = {"status":"", "title":"","content":""};
	
	$scope.createUser = function(signupData) {
		ajaxCallService.postData("/api/signup", signupData)
			.success(function (response) {
				
				if(response.status == "SUCCESS") {
					$location.path("/home");
					
					message.status="success";
					message.title=response.status;
					message.content=response.message;
					
					toasterService.popMessage(message);
				}
				else {
					
				}
			})
		    .error(function(err){
		    	
		    });
	}
});

