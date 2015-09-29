from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Player)
admin.site.register(User)
admin.site.register(Bot)
admin.site.register(Insults)
admin.site.register(LeaderBoard)