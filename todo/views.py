from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *


# @api_view(['GET', 'POST'])
# def todo_list_create(request: Request):
#     if request.method == 'GET':
#         todos = Todo.objects.order_by('priority')
#         todo_serializer = TodoSerializer(instance=todos, many=True)
#         return Response(data=todo_serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == 'POST':
#         todo_serializer = TodoSerializer(data=request.data)
#         if todo_serializer.is_valid():
#             todo_serializer.save()
#             return Response(data=todo_serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(data=None, status=status.HTTP_400_BAD_REQUEST)
#
#     else:
#         return Response(data=None, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def todo_detail_update_delete(request: Request, todo_id):
#     try:
#         todo = Todo.objects.get(id=todo_id)
#     except Todo.DoesNotExist:
#         return Response(data=None, status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         todo_serializer = TodoSerializer(instance=todo)
#         return Response(data=todo_serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == 'PUT':
#         todo_serializer = TodoSerializer(instance=todo, data=request.data)
#         if todo_serializer.is_valid():
#             todo_serializer.save()
#             return Response(data=todo_serializer.data, status=status.HTTP_202_ACCEPTED)
#         else:
#             return Response(data=None, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         todo.delete()
#         return Response(data=None, status=status.HTTP_204_NO_CONTENT)
#
#     else:
#         return Response(data=None, status=status.HTTP_400_BAD_REQUEST)


class TodoListCreateView(APIView):
    def get(self, request: Request):
        todos = Todo.objects.order_by('priority')
        todo_serializer = TodoSerializer(instance=todos, many=True)
        return Response(data=todo_serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request):
        todo_serializer = TodoSerializer(data=request.data)
        if todo_serializer.is_valid():
            todo_serializer.save()
            return Response(data=todo_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=None, status=status.HTTP_400_BAD_REQUEST)


class TodoDetailUpdateDeleteView(APIView):

    def dispatch(self, request: Request, *args, **kwargs):
        try:
            self.instance_todo = Todo.objects.get(id=kwargs.get('todo_id'))
        except Todo.DoesNotExist:
            return Response(data=None, status=status.HTTP_404_NOT_FOUND)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request: Request, *args, **kwargs):
        todo_serializer = TodoSerializer(instance=self.instance_todo)
        return Response(data=todo_serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, *args, **kwargs):
        todo_serializer = TodoSerializer(instance=self.instance_todo, data=request.data)
        if todo_serializer.is_valid():
            todo_serializer.save()
            return Response(data=todo_serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(data=None, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, *args, **kwargs):
        self.instance_todo.delete()
        return Response(data=None, status=status.HTTP_204_NO_CONTENT)
