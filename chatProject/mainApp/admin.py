from django.contrib import admin

# Register your models here.
from .models import Posts, Tags

admin.site.register(Posts)
admin.site.register(Tags)
