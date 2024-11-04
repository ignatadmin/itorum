from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Mailing
from .tasks import start_mailing
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Mailing)
def schedule_mailing(sender, instance, **kwargs):
    if instance.start_time <= timezone.now() <= instance.end_time:
        start_mailing.delay(instance.id)
    else:
        logger.info(f"Время начала рассылки с ID {instance.id} истекло, запуск невозможен.")
