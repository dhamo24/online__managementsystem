from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("admin_login/", views.admin_login, name="admin_login"),
    path("student_registration/", views.student_registration, name="student_registration"),
    path("student_login/", views.student_login, name="student_login"),
    ]