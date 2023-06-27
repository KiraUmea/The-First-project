from django.db import models

# Create your models here.
class User(models.Model):
    name = models.TextField(max_length=50)


class Topic(models.Model):
    title = models.TextField(max_length=50)
    description = models.TextField(max_length=150)


class Post(models.Model):
    slug = models.SlugField(unique = True, blank = True, null = True)
    title = models.TextField(max_length=100)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateField()
    updated_at = models.DateField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    topic = models.ManyToManyField(Topic)


class Comment(models.Model):
    created_at = models.DateField()
    content = models.TextField(max_length=400)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='posts')


#class User(models.Model):

