from django.urls import path
from .views import home,about,postcreate,frontend_postcreate

urlpatterns = [
    path("", home, name="home"),
    path("about/",about,name= "about"),
    path("create/",postcreate,name="create-post"),
    path("frontend/",frontend_postcreate,name="frontend")
]