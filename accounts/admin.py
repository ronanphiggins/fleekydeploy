from django.contrib import admin
from .models import User, Crush, Status, Likers, Wink

admin.site.register(User)
admin.site.register(Crush)
admin.site.register(Status)
admin.site.register(Likers)
admin.site.register(Wink)
