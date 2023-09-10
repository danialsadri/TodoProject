from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home),
    path('todos/list/', views.todos_list),
]
