"""
URL configuration for project_task project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from app1 import views
# from project import views
from app1 import views as views_app1
from project import views as views_project

urlpatterns = [
    path('admin/', admin.site.urls),
    path("signup/",views_app1.SignupPage, name='signup'),
    path("",views_app1.LoginPage, name='login'),
    path("home/",views_app1.HomePage, name='home'),
    path("logout/",views_app1.LoginPage, name='logout'),
    path('client-detail/', views_project.client_detail, name="client-D"),
     path('client-Add/', views_project.client_add, name="client-A"),
     path('client_delete(?C<int:cid>)',views_project.delete_client,name='delete_client'),
    path('client_edit/<int:eid>',views_project.client_edit, name="client-E"),
    path('user_detail/',views_project.User_detail, name="user_D"),
    path('user_delete(?U<int:uid>)',views_project.delete_user,name="delete_user"),
    path('user-add/',views_project.user_add,name="user-A"),
    path('user_edit/<int:UEid>',views_project.user_edit, name="user-E"),
    path('project-tabel',views_project.Project_table,name='project-t'),
    path('project_detail/',views_project.project_detail,name="project-D"),
    path('project_add',views_project.project_add,name="project-A"),
    path('project_delete(?U<int:pid>)',views_project.delete_project,name="delete_project"),
]
