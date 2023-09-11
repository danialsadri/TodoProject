from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    priority = models.IntegerField(default=1)
    is_done = models.BooleanField(default=False)

    class Meta:
        db_table = 'todos'

    def __str__(self):
        return self.title
