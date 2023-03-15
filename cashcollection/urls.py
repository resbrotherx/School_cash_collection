from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'new'

urlpatterns = [
    path('', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('create', views.create, name="create"),
    path('create_class', views.create_class, name="create_class"),
    path('creat_class_api', views.creat_class_api, name="creat_class_api"),
    path('creat_student_api', views.creat_student_api, name="creat_student_api"),
    path('log', views.log, name="log"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('all_student', views.all_student, name="all_student"),
    path('all_class/', views.all_classes, name="all_classes"),
    path('create_student', views.create_student, name="create_student"),
    # path('contact/', views.contact, name="contact"),
    # path('news_detail/<id>/', views.news_detail, name='news_detail'),
]