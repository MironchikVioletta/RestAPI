from django.shortcuts import render
from rest_framework import viewsets, filters

from .serializers import TaskSerializers
from .models import Task


class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializers

    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter)
    filter_fields = ('completed',)
    ordering = ('-date_created')

# there are possibilities to make one class using filters
# in queryset queryset = Task.objects.all().order_by('-date_created')

# class DueTaskViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all().order_by('-date_created').filter(completed = False)
#     serializer_class = TaskSerializers
#
# class CompletedTaskViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all().order_by('-date_created').filter(completed = True)
#     serializer_class = TaskSerializers


