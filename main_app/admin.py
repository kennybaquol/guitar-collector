from django.contrib import admin
# import your models here
from .models import Guitar, Tuned, Player
# Register your models here.
admin.site.register(Guitar)
admin.site.register(Tuned)
admin.site.register(Player)