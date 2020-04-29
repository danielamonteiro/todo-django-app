from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Tasks(models.Model):
    STATUS_CHOICES = (
    ('Completed', 'Completed'),
    ('Pending', 'Pending'),
    ('Canceled', 'Canceled'))

    task_name = models.CharField(max_length=200)
    category = models.CharField(max_length=100, default="Undefined")
    description = models.TextField(blank=True, null=True)
    deadline = models.DateTimeField()
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default="Pending")
    creation_date = models.DateTimeField(auto_now=True)
    task_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_name

    def get_task_deadline(self):
        return self.deadline.strftime('%d/%m/%Y - %H:%M')
    
    def get_creation_date(self):
        return self.creation_date.strftime('%Y-%m-%dT%H:%M')
    
    def get_data_input_task(self):
        # formato padrão para o input datetime-local
        return self.deadline.strftime('%Y-%m-%dT%H:%M')
    
    def get_late_tasks(self):
        if self.deadline < datetime.now():
            return True
        else:
            return False
    
    def get_pending_tasks(self):
        if self.status == "Pending":
            return True
        else:
            return False
