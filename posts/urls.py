from django.urls import path
from . import  views
urlpatterns = [

    path('list', views.PostListView.as_view(),name="post-list")

]
