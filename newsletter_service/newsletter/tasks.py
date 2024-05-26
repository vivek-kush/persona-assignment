# tasks.py
from celery import shared_task
from django.core.mail import send_mail
from .models import Content
from newsletter_service.settings import EMAIL_HOST_USER

@shared_task
def send_emails_to_subscribers(content_id):
    content = Content.objects.get(id=content_id)
    subscribers = content.topic.subscriber_set.all()
    subscriber_emails = [subscriber.email for subscriber in subscribers]
    send_mail(
        subject=f"New content on {content.topic.name}",
        message=content.text,
        from_email=EMAIL_HOST_USER,
        recipient_list=subscriber_emails,
        fail_silently=False
    )
