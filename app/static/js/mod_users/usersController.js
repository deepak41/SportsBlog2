app.service("getService", function($http) {
	
	this.getData = function(url) {
		return $http.get(url);
	}
});


app.controller("userhomeCtrl", function($scope, getService) {
	
	getService.getData("/api/userhome")
		.success(function(response){
			$scope.latestPosts = response["section1"];
			$scope.sectionalPosts = response["section2"];
		})
	
})