from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView 
from rest_framework.viewsets import ModelViewSet
#my imports
from .models import Task
from .serializers import TaskSerializer 


@api_view(["GET", "POST"])
def task_list_create(request):
    if request.method == "GET":
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data) 
        
    if request.method == "POST":
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "DELETE", "PUT"])
def task_detail(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "GET":
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = TaskSerializer(data=request.data, instance = task)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        task.delete()
        return Response({"message": "Task has been deleted!"})
    
class Tasks(ListCreateAPIView):
    queryset= Task.objects.all()
    serializer_class = TaskSerializer
    
    
    
class TaskDetail(RetrieveUpdateAPIView):
    queryset= Task.objects.all()
    serializer_class = TaskSerializer


class TaskMVS(ModelViewSet):
    queryset= Task.objects.all()
    serializer_class = TaskSerializer
