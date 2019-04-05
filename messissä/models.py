from django.db import models

class Tapahtuma(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.CharField(max_length=30)

    def __str__(self):
        return self.name
        