from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    topics = models.ManyToManyField(Topic)

    def __str__(self):
        return self.email

class Content(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    send_time = models.DateTimeField()

    def __str__(self):
        return f"{self.topic.name} - {self.send_time}"
