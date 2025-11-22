from django.urls import path
from . import views

appname = "employees"

urlpatterns = [
    path('', views.home, name="employees"),
]
