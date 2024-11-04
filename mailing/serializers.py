import re
from rest_framework import serializers
from .models import Client, Mailing, Message

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

    def validate_phone_number(self, value):
        pattern = re.compile(r'^7\d{10}$')
        if not pattern.match(value):
            raise serializers.ValidationError(
                f"Номер '{value}' должен быть в формате '7xxxxxxxxxx', где x - цифра от 0 до 9."
            )
        return value


class MailingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailing
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
