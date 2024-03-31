from django.db import models


class Channel(models.Model):
    name = models.CharField(max_length=32)
    chat_id = models.BigIntegerField(unique=True)
    is_group = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
