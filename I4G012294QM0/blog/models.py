from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    Published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title