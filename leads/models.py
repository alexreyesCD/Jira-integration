from django.db import models


class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    note = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)