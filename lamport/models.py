from django.db import models

class LamportUser(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password_hash = models.CharField(max_length=64)  # Assuming SHA-256 for simplicity
    hash_iterations = models.IntegerField(default=100)