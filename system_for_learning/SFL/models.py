from django.db import models

# Create your models here.
class NewsOfSite(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=False, blank=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True)