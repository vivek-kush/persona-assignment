from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

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

@receiver(post_save, sender=Content)
def schedule_email_task(sender, instance, created, **kwargs):
    if created:
        from .tasks import send_emails_to_subscribers
        # Schedule the Celery task to send emails at the specified send_time
        send_time = instance.send_time
        send_emails_to_subscribers.apply_async(args=[instance.id], eta=send_time)
