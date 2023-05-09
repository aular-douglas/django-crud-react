
from rest_framework import viewsets
from .serializer import TaskSerealizer
from .models import Task

# Create your views here.
class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerealizer
    queryset = Task.objects.all()
