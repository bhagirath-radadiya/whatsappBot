from django.urls import path
from . import views

urlpatterns = [
    path('modelBot', views.modelBot, name='modelBot'),

    path('view', views.view, name='view'),
    path('insert', views.insert, name='insert'),
    path('edit', views.edit, name='edit'),
    path('update', views.update, name='update'),
    path('delete', views.delete, name='delete'),

    path('deleteFile', views.deleteFile, name='deleteFile'),

]
