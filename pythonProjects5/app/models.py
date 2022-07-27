from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    password = models.IntegerField(blank=True, null=True)
    user = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
