from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="core/login.html"), name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("post/new/", views.post_create, name="post_create"),
    path("post/<int:id>/", views.post_detail, name="post_detail"),
    path("post/<int:id>/edit/", views.post_update, name="post_update"),
    path("post/<int:id>/delete/", views.post_delete, name="post_delete"),
    path("post/search/", views.post_search, name="search"),
    path("users/search/", views.user_search, name="user_search"),
    path("profile/<str:username>/", views.profile_view, name="profile"),
]

