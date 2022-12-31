from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name='index'),
    path("deleteNote/<id>", views.deleteNote, name="deleteNote")
]
