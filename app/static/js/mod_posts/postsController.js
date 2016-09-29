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


app.controller("latestNewsCtrl", function($scope, $location, $routeParams, ajaxCallService, checkNumberService) {
	
	var area = $routeParams.area;
	var region = $routeParams.region;
	$scope.region = region;
	
	var page = $location.search().page;
	
	if(page == undefined) {
		page = 1;
	}
	else if(!checkNumberService.isInt(page)) {
		$location.path("/404");
	}
	
	page = parseInt(page);
	
	var url = "";
	if(area == undefined && region == undefined) {
		url = "/api/get_latestposts?page=";
		$scope.paginationUrl = "#/latest_news?page=";  
	}
	else if(area != undefined && region == undefined) {
		url = "/api/get_latestposts/"+ area +"?page=";
		$scope.paginationUrl = "#/latest_news/"+ area +"?page="; 
	}
	else {
		url = "/api/get_latestposts/"+ area +"/" + region +"?page=";
		$scope.paginationUrl = "#/latest_news/"+ area +"/" + region +"?page=";
		
		$scope.region = region.toUpperCase();
		if(region == "southamerica"){
			$scope.region = "SOUTH AMERICA";
		}
	}
	
	
	ajaxCallService.getData(url + page)
	.success(function(response) {
		$scope.posts = response;
		console.log(response);
	});
	
	
	$scope.nextpage = page+1;
	$scope.previous = page-1;
    if ($scope.previous < 1) {
    	$scope.previous = 1;
    }
    
	
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