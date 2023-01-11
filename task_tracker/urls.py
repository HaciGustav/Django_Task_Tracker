
from django.urls import path, include
from .views import (task_list_create, task_detail, Tasks, TaskDetail)

urlpatterns = [
    # path("/create/", task_list_create),
    # path("detail/<int:id>", task_detail),  
    path("create/", Tasks.as_view()),
    path("detail/<int:pk>", TaskDetail.as_view()),
]
