from heyoo import WhatsApp
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order

@receiver(post_save, sender=Order)
def send_order_notification(sender, instance, created, **kwargs):
    if created:
        message = f"New order placed! Order ID: {instance.id}, sender phone: {instance.phone}, sender name: {instance.name},vendor phone: {instance.house.owner.phone},vendor name: {instance.house.owner.name}"
        recipient_id = '+249127958201'  # Replace with the admin's WhatsApp number
        send_whatsapp_message(message, recipient_id)

def send_whatsapp_message(message, recipient_id):
    messenger = WhatsApp(settings.WHATSAPP_ACCESS_TOKEN, phone_number_id=settings.WHATSAPP_PHONE_NUMBER_ID)
   
    response = messenger.send_message(message, recipient_id)
    return response