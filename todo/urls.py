from django.urls import path
from . import views


app_name = 'todo'
urlpatterns = [
    # path('list_create/', views.todo_list_create),
    # path('detail_update_delete/<int:todo_id>/', views.todo_detail_update_delete),
    path('list_create/', views.TodoListCreateView.as_view()),
    path('detail_update_delete/<int:todo_id>/', views.TodoDetailUpdateDeleteView.as_view()),
]
