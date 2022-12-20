from __future__ import unicode_literals

from django.db import models


class Software(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return self.name
