from django.urls import path
from . import views

app_name="core_"
urlpatterns = [
    path('', views.frontpage, name="frontpage"),
]



