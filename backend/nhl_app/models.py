from django.db import models

class League(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class Conference(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name="conferences")
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class Division(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name="divisions")
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE, related_name="divisions")
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class Team(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name="teams")
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE, related_name="teams")
    division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name="teams")
    name = models.CharField(max_length=100)
    gp = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    ot = models.IntegerField(default=0)

    @property
    def points(self):
        points = (self.wins * 2) + self.ot
        return points

    def __str__(self):
        return f"{self.name}"

class Player(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name="players")
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE, related_name="players")
    division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name="players")
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="players")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gp = models.IntegerField(default=0)
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)

    @property
    def points(self):
        points = self.goals + self.assists
        return points

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
