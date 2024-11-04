from celery import shared_task
from datetime import timedelta
import logging
from django.utils import timezone
from .models import Mailing, Message, Client

logger = logging.getLogger(__name__)


@shared_task
def start_mailing(mailing_id):
    try:
        mailing = Mailing.objects.get(id=mailing_id)
    except Mailing.DoesNotExist:
        logger.info(f"Рассылка с ID {mailing_id} не найдена.")
        return

    if timezone.now() > mailing.end_time:
        logger.info(f"Время окончания рассылки с ID {mailing_id} прошло. Отправка остановлена.")
        return

    clients = Client.objects.filter(
        operator_code=mailing.filter_operator_code,
        tag=mailing.filter_tag
    )

    if not clients.exists():
        logger.info(f"Для рассылки с ID {mailing_id} нет подходящих клиентов.")
        return

    for client in clients:
        if timezone.now() > mailing.end_time:
            logger.info(f"Время окончания рассылки с ID {mailing_id} прошло. Завершаем отправку.")
            break

        try:
            message = Message.objects.create(mailing=mailing, client=client)
            logger.info(f"Сообщение отправлено на {client.phone_number}: {mailing.text_message}")
        except Exception as e:
            logger.error(f"Ошибка при отправке сообщения на {client.phone_number}: {e}")


@shared_task
def check_upcoming_mailings():
    now = timezone.now()
    upcoming_mailings = Mailing.objects.filter(start_time__gt=now)

    for mailing in upcoming_mailings:
        if mailing.start_time - now <= timedelta(minutes=1) and now <= mailing.end_time:
            logger.info(f"Задача запущена для рассылки с ID {mailing.id}. Начало: {mailing.start_time}.")
            start_mailing.delay(mailing.id)
