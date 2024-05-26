# tasks.py
from celery import shared_task
from django.core.mail import send_mail
from .models import Content

@shared_task
def send_emails_to_subscribers(content_id):
    content = Content.objects.get(id=content_id)
    subscribers = content.topic.subscriber_set.all()
    subscriber_emails = [subscriber.email for subscriber in subscribers]
    send_mail(
        subject=f"New content on {content.topic.name}",
        message=content.text,
        from_email="vivekkushtest@gmail.com",
        recipient_list=subscriber_emails,
        fail_silently=False
    )
