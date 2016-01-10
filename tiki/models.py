from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    pub_date = models.DateField()
    category = models.CharField(max_length=50)
    hero_image = models.FileField()
    extra_image = models.FileField(blank=True)
    body_text = models.TextField()



