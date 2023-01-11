from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = (
            "id",
            "task",
            "description",
            "priority",
            "is_done",
            "created_date",
            "updated_date"
        )