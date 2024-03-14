from django.urls import path
from . import views
urlpatterns=[
    path ('', views.homee, name = "home"),
    path ('register/', views.registerPage, name = 'register'),
    path ('login/', views.loginPage, name = "login"),
    path ('logout/', views.logoutPage, name = "logout"),
    path ('index/', views.index, name = "index"),
    path ('new/', views.new, name = "new" ),
    path ('subject/', views.subject, name="subject")
]