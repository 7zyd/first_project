from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator

class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='topics')
    starter = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='topics', null=True)

    def __str__(self):
        return self.subject

class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='posts', null=True)

    def __str__(self):
        truncated_message = Truncator(self.message)
        return truncated_message.chars(30)
