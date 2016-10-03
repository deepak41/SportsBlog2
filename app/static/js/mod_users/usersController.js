app.controller("userhomeCtrl", function($scope, ajaxCallService) {
	
	ajaxCallService.getData("/api/userhome")
		.success(function(response){
			
			if(response.status == "SUCCESS") {
				$scope.latestPosts = response.data["section1"];
				$scope.sectionalPosts = response.data["section2"];
			}
		})
});