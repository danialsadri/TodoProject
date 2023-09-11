from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


app_name = 'todo'
router = DefaultRouter()
router.register('', views.TodoViewSet)
urlpatterns = [
    # path('list_create/', views.todo_list_create),
    # path('detail_update_delete/<int:todo_id>/', views.todo_detail_update_delete),
    path('list_create/', views.TodoListCreateView.as_view()),
    path('detail_update_delete/<int:todo_id>/', views.TodoDetailUpdateDeleteView.as_view()),
    path('list_create_mixin/', views.TodoListCreateMixinView.as_view()),
    path('detail_update_delete_mixin/<int:todo_id>/', views.TodoDetailUpdateDeleteMixinView.as_view()),
    path('todo_list_create_concrete/', views.TodoListCreateConcreteView.as_view()),
    path('todo_detail_update_delete_concrete/<int:todo_id>/', views.TodoDetailUpdateDeleteConcreteView.as_view()),
    path('users/', views.UserListView.as_view()),
    path('viewset/', include(router.urls)),
]
