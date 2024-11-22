from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),

    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),

    path('update-user/', views.updateUser, name="update-user"),

    path('topics/', views.topicsPage, name="topics"),
    path('activity/', views.activityPage, name="activity"),



    path("goals/", views.goal_list, name="goal_list"),
    path("goals/new/", views.goal_create, name="goal_create"),
    path("tasks/new/<int:goal_id>/", views.task_create, name="task_create"),


    path('run-task/', views.run_task, name='run_task'),

    
    path('trigger-simple-task/', views.trigger_simple_task, name='trigger_simple_task'),
    path('trigger-send-task-reminders/', views.trigger_send_task_reminders, name='trigger_send_task_reminders'),
]
