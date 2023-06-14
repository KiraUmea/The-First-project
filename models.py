from django.db import models

# Create your models here.


class Topic(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=20)
    topics = models.ManyToManyField(Topic)


class Blogpost(models.Model):
    topics = models.ManyToManyField(Topic)
    text = models.TextField(null=True, blank=True, max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogposts')

    class Meta:
        ordering = ['text']

    def __str__(self):
        return self.text


class Comment(models.Model):
    text = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
