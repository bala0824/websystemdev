from django.db import models

class Channel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Video(models.Model):
    title = models.CharField(max_length=255)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    embed_code = models.TextField()

    def __str__(self):
        return self.title