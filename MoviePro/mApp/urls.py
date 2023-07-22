from django.urls import path
from mApp import views

urlpatterns = [
    
    path("pview/", views.display_movie),
    path("",views.display),
    path("pmovie",views.add_movie)
    
]