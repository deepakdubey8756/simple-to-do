from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Notes(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length =  200)
    description = models.TextField(default="none")
    isCompleted = models.BooleanField(default=False)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title