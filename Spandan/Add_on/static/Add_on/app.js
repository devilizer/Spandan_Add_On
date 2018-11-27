var app=angular.module("app",[]);

app.controller("myapp",["$scope","$http",function($scope,$http){



  $(function() {
    // page is now ready, initialize the calendar...
    $(document).ready(function(){
      var date = new Date();
      var d = date.getDate();
      var m = date.getMonth();
      var y = date.getFullYear();



    });

    $('#calendar').fullCalendar({
      // put your options and callbacks here

      defaultView: 'agendaFourDay',
      groupByResource: true,
      selectable : true,
      droppable : true,
      allDay : false,
      selectHelper: true,
      editable: true,
      eventLimit: true, // allow "more" link when too many events
      header: {
        left: 'prev,next',
        center: 'title',
        right: 'agendaDay,agendaFourDay'
      },
      views: {
        agendaFourDay: {
          type: 'agenda',
          duration: { days: 4 }
        }
      },

      select: function(start, end) {
                // Display the modal.
                // You could fill in the start and end fields based on the parameters
                $('.modal').modal('show');

      },
      eventClick: function(event, element) {
                // Display the modal and set the values to the event values.
                $('.modal').modal('show');
                $('.modal').find('#title').val(event.title);
                $('.modal').find('#starts-at').val(event.start);
                $('.modal').find('#ends-at').val(event.end);
      }



      });


    // Bind the dates to datetimepicker.
    // You should pass the options you need
    $("#starts-at, #ends-at").datetimepicker();

    // Whenever the user clicks on the "save" button om the dialog
    $('#save-event').on('click', function() {
        var title = $('#title').val();
        if (title) {
            var eventData = {
                title: title,
                start: $('#starts-at').val(),
                end: $('#ends-at').val(),
                sport_id : sport1_id,
                team1_id : team1_id,
                team2_id : team2_id ,
                level : level_1
            };

            $('#calendar').fullCalendar('renderEvent', eventData, true); // stick? = true
        }
        $('#calendar').fullCalendar('unselect');

        // Clear modal inputs
        $('.modal').find('input').val('');

        // hide modal
        $('.modal').modal('hide');
    });

      $('#calendar').fullCalendar('next');


    });

    $http.get('/Schedule/matches/').then(function(response){
      $scope.matchlist = response.data;
      console.log(response.data);
    });

    $http.get('/Schedule/teams/').then(function(response){
      $scope.teamlist = response.data;
      console.log(response.data);
    });

    $http.get('/Schedule/sports/').then(function(response){
      $scope.sportlist = response.data;
      console.log(response.data);
    });



    $scope.sports_names=[
      {
        "sport_id":"0",
        "sport_name":"Please select The Sport"
      },
      {
        "sport_id":"1",
        "sport_name":"Badminton"
      },
      {
        "sport_id":"2",
        "sport_name":"Cricket"
      },
      {
        "sport_id":"3",
        "sport_name":"Volleyball"
      },
      {
        "sport_id":"4",
        "sport_name":"Table Tennis"
      }

    ];

    $scope.teams_names=[
      {
        "team_id":"0",
        "team_name":"Please select The Team"
      },
      {
        "team_id":"1",
        "team_name":"Team1"
      },
      {
        "team_id":"2",
        "team_name":"Team2"
      }
    ];


      $scope.match_names=[

      ];

      var eventbyteam = function(teamname){


      };




}]);
