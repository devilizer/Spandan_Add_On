var myfirstmodule = angular.module("myfirstmodule",['ngRoute']);

myfirstmodule.config(['$routeProvider',function($routeProvider){

  $routeProvider
    .when('/page1',{
      templateUrl: 'HTML_Files/page1.html',
      controller: 'FirstControl'
    })
    .when('/frontend',{
      templateUrl: 'HTML_Files/frontendday1.html'
    }).otherwise({
      redirectTo : '/page1'
    })






}]);

myfirstmodule.controller("FirstControl",["$scope" ,function($scope){
  $scope.message = "This is it";
  $scope.removeninja = function(ninja){
    var removedninja = $scope.ninjas.indexOf(ninja);
    $scope.ninjas.splice(removedninja,1);
  };

  $scope.addNinja =  function(){

    $scope.ninjas.push({

      name:$scope.newninja.name,
      belt:$scope.newninja.belt,
      rate:parseInt($scope.newninja.rate),
      available:true

    });

    $scope.newninja.name= "";
    $scope.newninja.belt= "";
    $scope.newninja.rate= "";

  };

  $scope.ninjas = [
    {
      name:"Karan",
      belt:"blue",
      rate:5000,
      available:true
    },
    {
      name:"Kartik",
      belt:"red",
      rate:100,
      available:true
    },
    {
      name:"ThirdOne",
      belt:"green",
      rate:500,
      available:false
    }
  ];

  console.log(angular.toJson($scope.ninjas))

}]);
