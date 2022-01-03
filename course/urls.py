from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register, name="register"),
    path('courses/', views.courses, name="courses"),
    path('topics/<str:courseid>/', views.topics, name="topics"),
    path('topics/<str:courseid>/<str:topicid>/', views.video, name="video"),
]
