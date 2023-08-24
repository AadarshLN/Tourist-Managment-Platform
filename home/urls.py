from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name= 'home'),
    path("home/",views.index,name= 'home'),
    path("about/",views.about,name='about'),
    path("contact/",views.contact,name= 'contact'),
    path("login/",views.login,name="login"),
    path("choice_of_login_page/",views.choice_of_login_page,name="choice_of_login_page"),
    path("profile/",views.profile,name="profile"),
    path("wish_list/",views.wish_list,name="wish_list"),
    
]
