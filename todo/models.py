from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    priority = models.IntegerField(default=1)
    is_done = models.BooleanField(default=False)

    class Meta:
        db_table = 'todos'

    def __str__(self):
        return self.title
