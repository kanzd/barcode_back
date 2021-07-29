from django.urls import path
from . import views
urlpatterns = [
    path("login/",views.LoginApiView.as_view()),
    path("loginvalidate/",views.LoginValidateApiView.as_view())
]