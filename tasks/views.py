from rest_framework.response import Response
from rest_framework import viewsets
from .models import Task
from .serializer import TaskSerializer
from django.utils import timezone

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
  queryset = Task.objects.all()
  serializer_class = TaskSerializer

  def list(self, request, *args, **kwargs):
    status_filter = request.GET.get('status')

    if status_filter:
      if status_filter == "incoming":
          tasks = self.queryset.filter(due_date__gt=timezone.now().date())
      elif status_filter == "today":
          tasks = self.queryset.filter(due_date=timezone.now().date())
      elif status_filter == "overdue":
          tasks = self.queryset.filter(due_date__lt=timezone.now().date())
    else:
        tasks = self.queryset

    serializer = self.get_serializer(tasks, many=True)
    return Response(serializer.data)
