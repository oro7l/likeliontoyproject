from django.contrib import admin
from django.urls import path
from posts.views import *

urlpatterns = [
    path('new/', create_post, name="create_post"),
    path('', get_post_all, name="get_post_all"),
    path('<int:id>/', delete_post, name="delete_post")
]
