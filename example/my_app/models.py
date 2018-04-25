from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    NEW = 1
    IN_PROGRESS = 2
    DONE = 3

    LOW = 1
    AVERAGE = 2
    HIGH = 3

    STATUS_CHOICE = (
        (NEW, 'New'),
        (IN_PROGRESS, 'In Progress'),
        (DONE, 'Done')
    )

    PRIORITY_CHOICE = (
        (LOW, 'Low'),
        (AVERAGE, 'Average'),
        (HIGH, 'High')
    )

    name = models.CharField(max_length=100)
    status = models.IntegerField(choices=STATUS_CHOICE, default=NEW)
    priority = models.IntegerField(choices=PRIORITY_CHOICE, default=LOW)
    description = models.TextField()
    team_lead_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
