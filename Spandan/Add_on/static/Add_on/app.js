var app=angular.module("app",[]);

app.controller("myapp",["$scope","$http","$q",function($scope,$http,$q){








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



          var msg = $.ajax({type: "GET", url: "/Schedule/matches/", async: false}).responseText;
          var jsonResponse = JSON.parse(msg);
          console.log(jsonResponse["data"]);
          jsonResponse=jsonResponse["data"];
          console.log(jsonResponse);
          var matchlist = jsonResponse;
          var matchlist1 = {};
          var matchlist2 = [];
          var len1 = matchlist.length;
          for(i=0;i<len1;i++){
            matchlist1[i] = {};
          }
          console.log(matchlist);
          for(i=0;i<len1;i++){
            var y = matchlist[i].Sport;
            var z = matchlist[i].id;
            matchlist1[i]["title"]="Match".concat((z.toString()));
            matchlist1[i]["type"]="agenda";
            matchlist1[i]["allDay"]="false";
            matchlist1[i]["start"]=matchlist[i]["start_time"];
            matchlist1[i]["end"]=matchlist[i]["end_time"];
            matchlist2.push(matchlist1[i]);
          }
          matchlist2=angular.toJson(matchlist2);
          console.log(matchlist2);
          var events = JSON.parse(matchlist2);




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
          duration: { days: 3 }
        }
      },

      events : events  ,

      select: function(start, end) {
                // Display the modal.
                // You could fill in the start and end fields based on the parameters
                $('.modal').modal('show');

    },


      eventClick: function(event, element) {
                // Display the modal and set the values to the event values.
                $('.modal').modal('show');
                $('.modal').find('#title').val(event.title);

      },



      });


    // Bind the dates to datetimepicker.
    // You should pass the options you need


    // Whenever the user clicks on the "save" button om the dialog
    $('#save-event').on('click', function() {
        var title = $('#title').val();
        if (title) {
          $.ajax({
              type : "POST",
              url : "/Schedule/matches/",
              csrfmiddlewaretoken: "{{ csrf_token }}",
              async : false,
              headers: {
                  'Content-Type': 'application/json'
              },
              data :angular.toJson([
                {
                  "Sport" : parseInt($('#sport1_id').val()),
                  "Team1" : parseInt($('#team1_id').val()),
                  "Team2" : parseInt($('#team2_id').val()),
                  "end_time" : $('#ends-at').val(),
                  "id" :  parseInt($('#team1_id').val()) + parseInt($('#team2_id').val()),
                  "level" : $('#level_1').val(),
                  "result" : $('#result_name').val(),
                  "start_time": $('#starts-at').val()
                }
              ]),

              success: function(){
                alert("Saved! It worked.");
              },
              error: function(XMLHttpRequest, textStatus, errorThrown) {
                alert("some error " + String(errorThrown) + String(textStatus) + String(XMLHttpRequest.responseText));
              }
            });

        }
        //$('#calendar').fullCalendar('renderEvent', eventmatches , true); // stick? = true
        $('#calendar').fullCalendar('unselect');

        // Clear modal inputs
        $('.modal').find('input').val('');

        // hide modal
        $('.modal').modal('hide');
    });

      $('#calendar').fullCalendar('next');




    });







}]);
