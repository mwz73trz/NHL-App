from django.contrib import admin
from nhl_app.models import League, Conference, Division, Team, Player

admin.site.register(League)
admin.site.register(Conference)
admin.site.register(Division)
admin.site.register(Team)
admin.site.register(Player)
