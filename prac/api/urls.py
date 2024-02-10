from home.views import store,index,LoginApi,RegisterApi
from django.urls import path

urlpatterns = [
    path("",index),
    path("store/",store),
    path("login/",LoginApi.as_view()),
    path("register/",RegisterApi.as_view())
]