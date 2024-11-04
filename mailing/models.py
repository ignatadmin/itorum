from django.db import models


class Client(models.Model):
    phone_number = models.TextField(max_length=11, unique=True)
    operator_code = models.TextField(max_length=3)
    tag = models.TextField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.phone_number} ({self.tag})"


class Mailing(models.Model):
    text_message = models.TextField()
    filter_operator_code = models.TextField(max_length=3, blank=True)
    filter_tag = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return (f"ID: {self.id} - Начало: {self.start_time} Конец: {self.end_time} - \n"
                f"Тег: {self.filter_tag} - Оператор: {self.filter_operator_code}")


class Message(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.id} - Номер: {self.client.phone_number} - \n"
                f"Сообщение: {self.mailing.id} - \n"
                f"Дата отправки: {self.created_at}")
