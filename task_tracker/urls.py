
from django.urls import path, include
from rest_framework import routers
from .views import (task_list_create,
                    task_detail,
                    Tasks,
                    TaskDetail,
                    TaskMVS)

router = routers.DefaultRouter()
router.register("task", TaskMVS)

urlpatterns = [
    # path("/create/", task_list_create),
    # path("detail/<int:id>", task_detail),  
    # path("create/", Tasks.as_view()),
    # path("detail/<int:pk>", TaskDetail.as_view()),
    path("", include(router.urls))
]
