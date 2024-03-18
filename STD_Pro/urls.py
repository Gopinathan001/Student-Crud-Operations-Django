"""
URL configuration for STD_Pro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from STD_App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    # section
    path('section/', views.section, name="section"),
    path('All_section/', views.All_section, name="All_section"),
    path('sections_student_detail/<int:section_id>/', views.view_section, name='view_section'),
    path('update_section/<int:sec_id>/', views.edit_section, name="edit_section"),
    path('delete_section/<int:sec_id>/', views.delete_section, name="delete_section"),
    
    # student
    path('sections/<int:section_id>/students/create/', views.student_data, name='student_data'),
    path('sections/<int:section_id>/students/<int:student_id>/update/', views.update_student, name='update_student'),
    path('sections/<int:section_id>/students/<int:student_id>/delete/', views.delete_student, name='delete_student'),
]
