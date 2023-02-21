from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile
from django.core.mail import send_mail


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create a user profile on each account creation"""
    if created:
        UserProfile.objects.create(created_by=instance)


@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    """Send a welcome email to all new users"""
    if created:
        subject = 'Welcome to Job-Board'
        message = f'Hi {instance.username}, Welcome to Job-Board!'  # TODO: Create an email template for this
        from_email = 'matingonk@gmail.com'
        recipient_list = [instance.email]
        send_mail(subject, message, from_email, recipient_list)
