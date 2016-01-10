from django.db import models


class Document(models.Model):
    docfile = models.FileField()
    optional_file = models.FileField(blank=True)


