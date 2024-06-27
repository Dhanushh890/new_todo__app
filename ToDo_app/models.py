from django.db import models

class ToDolist(models.Model):
    text=models.TextField()