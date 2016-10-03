app.controller("navbarCtrl", function($scope) {
	$scope.isLoggedIn = false;
	
	if(sessionInfo.userId != null) {
		$scope.isLoggedIn = true;
		$scope.firstname = "Hi "+ sessionInfo.firstname +"!";
	}
})