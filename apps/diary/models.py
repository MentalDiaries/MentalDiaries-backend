from django.db import models
from django.contrib.auth.models import User

class Entry(models.Model):
    entry_date_time = models.DateTimeField(auto_now_add=True)
    entry = models.TextField()
    entry_title = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    entry_id = models.PositiveBigIntegerField()

    def __str__(self):
        return self.user.username

class FinalRecordID(models.Model):
    final_id = models.PositiveBigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.user.username