from rest_framework import serializers
from .models import Chat, File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id',
                  'file']


class ChatSerializer(serializers.ModelSerializer):
    chatId = FileSerializer(read_only=True, many=True)
    class Meta:
        model = Chat
        fields = ['id',
                  'incommingMsg',
                  'reply',
                  'chatId']
