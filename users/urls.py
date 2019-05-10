from django.urls import path
from . import  views
urlpatterns = [

    path('sign-up/',views.create_user,name="user-create"),
    path('update/', views.update_profile,name="user-update")


]
