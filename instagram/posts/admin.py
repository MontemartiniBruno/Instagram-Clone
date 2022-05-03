from django.contrib import admin
from posts.models import User
# Register your models here.

@admin.register(User)
class PostUserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'email', 'country')
    list_display_links = ('pk', 'first_name')