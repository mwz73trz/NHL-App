from rest_framework.serializers import ModelSerializer
from nhl_app.models import League, Conference, Division, Team, Player

class LeagueSerializer(ModelSerializer):
    class Meta:
        model = League
        fields = ['id', 'name', 'conferences', 'divisions', 'teams', 'players']
        depth = 1
        

class ConferenceSerializer(ModelSerializer):
    class Meta:
        model = Conference
        fields = ['id', 'name', 'divisions', 'teams', 'players']

class DivisionSerializer(ModelSerializer):
    class Meta:
        model = Division
        fields = ['id', 'name', 'teams', 'players']

class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'gp', 'wins', 'losses', 'ot', 'points', 'players']

class PlayerSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'first_name', 'last_name', 'gp', 'goals', 'assists', 'points']




