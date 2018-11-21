from django.db import models

# Create your models here.
class Sport(models.Model):
    Name = models.CharField(max_length=200)
    organiser = models.CharField(max_length =200,default=0)
    organizer_rollno = models.CharField(max_length=200,default=0)
    def __str__(self):
        return (self.Name)

class Team(models.Model):
    team_name = models.CharField(max_length=200)
    captain_name = models.CharField(max_length=200)
    cap_rollno = models.CharField(max_length=200)
    cap_contactno = models.IntegerField()
    team_size = models.IntegerField(default=1)
    sports = models.ManyToManyField(Sport,verbose_name='list of sports played by this team')
    def __str__(self):
        return (self.team_name + " " + self.captain_name)

class Match(models.Model):
    Sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    Team1 = models.ForeignKey(Team, on_delete=models.CASCADE,related_name='team1')
    Team2 = models.ForeignKey(Team, on_delete=models.CASCADE)
    level = models.CharField(max_length=200)
    start_time = models.DateTimeField('start of match')
    end_time = models.DateTimeField('end of match')
    result = models.CharField(max_length=200)
    def __str__(self):
        return(self.Team1.team_name+" vs "+ self.Team2.team_name)
