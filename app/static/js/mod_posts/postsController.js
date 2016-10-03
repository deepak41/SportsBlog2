app.controller("viewPostCtrl", function($scope, $routeParams, ajaxCallService) {
	
	var postId = $routeParams.postid;
	
	ajaxCallService.getData("/api/post/"+postId)
		.success(function(response){
			if(response.status == "SUCCESS") {
				$scope.post = response.data[0];
			}
		})
		
	ajaxCallService.getData("/api/userhome")
		.success(function(response){
			if(response.status == "SUCCESS") {
				$scope.latestPosts = response.data["section1"];
			}
		})	
})


app.controller("latestNewsCtrl", function($scope, $location, $routeParams, ajaxCallService, checkNumberService) {
	
	var area = $routeParams.area;
	var region = $routeParams.region;
	var page = $location.search().page;
	
	$scope.region = region;
	$scope.loggedUserId = sessionInfo.userId;
	
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
		if(response.status == "SUCCESS") {
			$scope.posts = response.data;
		}
	});
	
	$scope.nextpage = page+1;
	$scope.previous = page-1;
    if ($scope.previous < 1) {
    	$scope.previous = 1;
    }
		
	
    ajaxCallService.getData("/api/userhome")
	.success(function(response){
		if(response.status == "SUCCESS") {
			$scope.latestPosts = response.data["section1"];
		}
	})

})


app.controller("writePostCtrl", function($scope, $location, ajaxCallService, toasterService) {
	
	var message = {"status":"", "title":"","content":""};
	
	$scope.createPost = function(formData) {
		ajaxCallService.postData("/api/createpost", formData)
			.success(function(response) {
				
				if(response.status == "SUCCESS") {
					$location.path("/home");
					message.status="success";
					message.title=response.status;
					message.content=response.message;
					
					toasterService.popMessage(message);
				}
			})
		    .error(function(err){
		    	
		    });
	}
	
	$scope.regions = [
	    { name: 'ASIA', value: 'asia' }, 
	    { name: 'AFRICA', value: 'africa' }, 
	    { name: 'EUROPE', value: 'europe' },
	    { name: 'SOUTH AMERICA', value: 'southamerica' }
    ];
})


app.controller("editPostCtrl", function($scope, $location, $routeParams, ajaxCallService, toasterService) {
	var message = {"status":"", "title":"","content":""};
	var postId = $routeParams.postid;
	
	ajaxCallService.getData("/api/post/"+postId)
	.success(function(response){
		if(response.status == "SUCCESS") {
			$scope.formData = {
				"post_content":response.data[0].post_content, 
				"subject": response.data[0].subject,
				"region": response.data[0].region
			};
		}
	})
	
	$scope.regions = [
	          	    { name: 'ASIA', value: 'asia' }, 
	          	    { name: 'AFRICA', value: 'africa' }, 
	          	    { name: 'EUROPE', value: 'europe' },
	          	    { name: 'SOUTH AMERICA', value: 'southamerica' }
	              ];
	
	$scope.editPost = function(formData) {
		ajaxCallService.postData("/api/editpost/"+postId, formData)
			.success(function(response) {
				
				if(response.status == "SUCCESS") {
					$location.path("/home");
					message.status="success";
					message.title=response.status;
					message.content=response.message;
					
					toasterService.popMessage(message);
				}
			})
		    .error(function(err){
		    	
		    });}
})












