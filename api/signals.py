from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
import requests
from .models import Order,Message

@receiver(post_save, sender=Order)
def send_order_notification(sender, instance, created, **kwargs):
    message = f"New order placed! Order ID: {instance.id}, sender phone: {instance.phone}, sender name: {instance.name},vendor phone: {instance.house.owner.phone},vendor name: {instance.house.owner.name}"

    url = f'https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': settings.TELEGRAM_CHAT_ID,
        'text': message,
    }
    response = requests.post(url, json=payload)
    return response.json()


@receiver(post_save, sender=Message)
def send_message_notification(sender, instance, created, **kwargs):
    message = f"{instance.phone}, message: {instance.message}"

    url = f'https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': settings.TELEGRAM_CHAT_ID,
        'text': message,
    }
    response = requests.post(url, json=payload)
    return response.json()
    
