from home.views import store,index,LoginApi,RegisterApi,PersonApi
from django.urls import path

urlpatterns = [
    path("",index),
    path("person/",PersonApi.as_view()),
    path("login/",LoginApi.as_view()),
    path("register/",RegisterApi.as_view())
]