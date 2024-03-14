from django.shortcuts import render
from .serializers import TaskSerializers, UserSerializer
from .models import Task
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView

# Create your views here.

class TaskViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all().order_by('-date_created')
    serializer_class = TaskSerializers


class DueTaskViewset(viewsets.ModelViewSet):
    serializer_class = TaskSerializers
    queryset = Task.objects.all().order_by('-date_created').filter(completed=False)


class CompletedTaskViewset(viewsets.ModelViewSet):
    serializer_class = TaskSerializers
    queryset = Task.objects.all().order_by('-date_created').filter(completed=True)


class CreateuserView(CreateAPIView):
    model=get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer