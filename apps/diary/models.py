from django.db import models
from django.contrib.auth.models import User

class Entry(models.Model):
    entry_date_time = models.DateTimeField(auto_now_add=True)
    entry = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.user.username
