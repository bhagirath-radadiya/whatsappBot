from django.urls import path
from . import views

urlpatterns = [


    path('chat', views.mybot, name='mybot'),

]
