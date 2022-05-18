from django.db import models
from django.conf import settings

USER_MODEL = settings.AUTH_USER_MODEL
# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField(null=False, blank=False)
    due_date = models.DateTimeField(auto_now=False, null=False)
    is_completed = models.BooleanField(default=False)
    project = models.ForeignKey(
        "projects.Project", related_name="tasks", on_delete=models.CASCADE
    )
    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        related_name="tasks",
        on_delete=models.SET_NULL,
    )
    description = models.CharField(max_length=200, null=True, blank=True)
    notes = models.CharField(max_length=400, null=True, blank=True)

    def __str__(self):
        return self.name
