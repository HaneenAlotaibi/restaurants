from email.policy import default
from typing import Any
from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name =models.CharField(max_length=30)
    description =models.TextField()
    # description =models.TextField(*args Any, **kwargs: Any) -> None
    opening_time= models.TimeField()
    closing_time=models.TimeField()
    created_at=models.DateTimeField()