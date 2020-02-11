from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('base.html', views.index, name='index'),
	path('test.html', views.test, name='test_url'),
	path('courses.html', views.courses, name='courses_url'),
	path('team.html/', views.team, name='team_url'),
	path('profile.html', views.profile, name='profile_url'),

]