from django.contrib import admin

from .models import Player, Team, User

admin.site.register(User)
admin.site.register(Team)
admin.site.register(Player)
