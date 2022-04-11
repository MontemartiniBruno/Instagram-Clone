from django.contrib import admin
from django.urls import path
from . import views as local_views
from posts import views as posts_views



urlpatterns = [
    path('', posts_views.welcome),
    path('admin/', admin.site.urls),
    path('hello_world', local_views.hello_world),
    path('hi/<str:name>/<int:age>/', local_views.hi),
    path('feed/', posts_views.newpost),


    
]
