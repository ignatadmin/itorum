# admin.py

from django.contrib import admin
from .models import Client, Mailing, Message


class ClientAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'operator_code', 'tag')


class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_message', 'start_time', 'end_time', 'filter_operator_code', 'filter_tag')


class MessageAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'mailing', 'client')


admin.site.register(Client, ClientAdmin)
admin.site.register(Mailing, MailingAdmin)
admin.site.register(Message, MessageAdmin)
