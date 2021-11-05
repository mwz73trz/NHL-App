from django.db.models.query import Prefetch
from rest_framework.viewsets import ModelViewSet
from nhl_app.serializers import LeagueSerializer, ConferenceSerializer, DivisionSerializer, TeamSerializer, PlayerSerializer
from nhl_app.models import League, Conference, Division, Team, Player

class LeagueViewSet(ModelViewSet):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer

class ConferenceViewSet(ModelViewSet):
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer

class DivisionViewSet(ModelViewSet):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer

class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class PlayerViewSet(ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
