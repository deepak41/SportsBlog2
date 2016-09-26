app.controller("viewPostCtrl", function($scope, $routeParams, getService) {
	
	var postId = $routeParams.postid;
	
	getService.getData("/post/"+postId)
		.success(function(response){
			$scope.post = response[0];
		})
})


app.controller("writePostCtrl", function($scope, $location, postService) {
	
	$scope.createPost = function(formData) {
		postService.postData("/api/createpost", formData)
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