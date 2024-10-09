from django.db import models
from django.utils import timezone

# Create your models here
class Task(models.Model):
  title  = models.CharField(max_length=200)
  description = models.TextField(blank=True, null=True)
  due_date = models.DateField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title
  
  @property
  def completed(self):
    if(self.due_date > timezone.now().date()):
      return "Incoming"
    elif(self.due_date == timezone.now().date()):
      return "Today"
    return "Overdue"