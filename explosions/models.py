from django.db import models

class Quarry(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        db_table = "quarry"
