from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Player)
admin.site.register(Bot)
admin.site.register(Insult)
admin.site.register(LeaderBoard)
admin.site.register(MyUser)