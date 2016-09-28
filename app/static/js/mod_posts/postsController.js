app.controller("viewPostCtrl", function($scope, $routeParams, ajaxCallService) {
	
	var postId = $routeParams.postid;
	
	ajaxCallService.getData("/api/post/"+postId)
		.success(function(response){
			$scope.post = response[0];
		})
		
	ajaxCallService.getData("/api/userhome")
		.success(function(response){
			$scope.latestPosts = response["section1"];
		})	
})


app.controller("writePostCtrl", function($scope, $location, ajaxCallService) {
	
	$scope.createPost = function(formData) {
		ajaxCallService.postData("/api/createpost", formData)
			.success(function(response) {
				console.log(response);
				
				if(response == "success") {
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
})


app.controller("editPostCtrl", function($scope) {
	
	$scope.mess = "sunny day";
})