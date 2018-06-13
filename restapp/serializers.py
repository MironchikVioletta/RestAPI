from rest_framework import serializers

from .models import Task


class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model= Task
        fields = ('id', 'task_name', 'task_desc', 'completed', 'date_created')
