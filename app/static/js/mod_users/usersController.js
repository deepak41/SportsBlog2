app.controller("userhomeCtrl", function($scope, ajaxCallService) {
	
	ajaxCallService.getData("/api/userhome")
		.success(function(response){
			$scope.latestPosts = response["section1"];
			$scope.sectionalPosts = response["section2"];
			
			console.log($scope.sectionalPosts);
		})
});