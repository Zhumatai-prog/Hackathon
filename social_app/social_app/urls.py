from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", views.login, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('', include('social.apps.django_app.urls', namespace='social')),
    path("", views.home, name="home"),
]
