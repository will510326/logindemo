from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.todo, name='todo'),
    path('view/<int:id>', views.view, name='view')
]
