from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name='index'),
    path("edit/<note_id>", views.edit, name="edit"),
    path("deleteNote/<id>", views.deleteNote, name="deleteNote"),
    path('accounts/signup/', views.signup_view, name="signup"),
    path('accounts/login/', views.login_view, name="login"),
    path('accounts/logout/', views.logout_view, name="logout"),
    path('done/<pk>', views.addConfirm, name="done")
]
