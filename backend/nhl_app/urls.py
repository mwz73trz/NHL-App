from django.urls import path, include
from rest_framework.routers import DefaultRouter
from nhl_app.views import LeagueViewSet, ConferenceViewSet, DivisionViewSet, TeamViewSet, PlayerViewSet

router = DefaultRouter()
router.register('leagues', LeagueViewSet, basename='league')
router.register('conferences', ConferenceViewSet, basename='conference')
router.register('divisions', DivisionViewSet, basename='division')
router.register('teams', TeamViewSet, basename='team')
router.register('players', PlayerViewSet, basename='player')

urlpatterns = [
    path('', include(router.urls)),
]