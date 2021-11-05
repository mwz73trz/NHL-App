from rest_framework.serializers import ModelSerializer
from nhl_app.models import League, Conference, Division, Team, Player

class PlayerSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'first_name', 'last_name', 'gp', 'goals', 'assists', 'points']

class TeamSerializer(ModelSerializer):
    players = PlayerSerializer(many=True, required=False)
    class Meta:
        model = Team
        fields = ['id', 'name', 'gp', 'wins', 'losses', 'ot', 'points', 'players']

class DivisionSerializer(ModelSerializer):
    teams = TeamSerializer(many=True, required=False)
    players = PlayerSerializer(many=True, required=False)
    class Meta:
        model = Division
        fields = ['id', 'name', 'teams', 'players']

class ConferenceSerializer(ModelSerializer):
    divisions = DivisionSerializer(many=True, required=False)
    teams = TeamSerializer(many=True, required=False)
    players = PlayerSerializer(many=True, required=False)
    class Meta:
        model = Conference
        fields = ['id', 'name', 'divisions', 'teams', 'players']

class LeagueSerializer(ModelSerializer):
    conferences = ConferenceSerializer(many=True, required=False)
    divisions = DivisionSerializer(many=True, required=False)
    teams = TeamSerializer(many=True, required=False)
    players = PlayerSerializer(many=True, required=False)
    class Meta:
        model = League
        fields = ['id', 'name', 'conferences', 'divisions', 'teams', 'players']
