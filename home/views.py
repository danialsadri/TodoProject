from django.shortcuts import render
from todo.models import *
from django.http import HttpRequest, JsonResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view


def home(request):
    todos = Todo.objects.order_by('priority')
    context = {'todos': todos}
    return render(request, 'home/home.html', context)


# def todos_list(request: HttpRequest):
#     todos = list(Todo.objects.order_by('priority').values('title', 'priority', 'is_done'))
#     return JsonResponse({'todos': todos})

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def todos_list(request: Request):
    todos = list(Todo.objects.order_by('priority').values('title', 'priority', 'is_done'))
    return Response({'todos': todos})
