from django.db import models

class ChatRoom(models.Model):
    name = models.CharField(max_length = 30)

class Message(models.Model):
    room = models.ForeignKey(ChatRoom)
    content = models.CharField(max_length = 300)
    author = models.CharField(max_length = 30)
