from django.db import models

# Create your models here.
class Products():
    title            = models.TextField()
    description      = models.TextField()
    price            = models.TextField()
    summary          = models.TextField()  