from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
  completed = serializers.ReadOnlyField()

  class Meta:
      model = Task
      fields = ['id', 'title', 'description', 'due_date', 'created_at', 'completed']