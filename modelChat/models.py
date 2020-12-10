from django.db import models

# Create your models here.

class Chat(models.Model):
    incommingMsg = models.CharField(max_length=500)
    reply = models.CharField(max_length=100000)

    def __str__(self):
        return self.incommingMsg

class File(models.Model):
    file = models.FileField()
    chatId = models.ForeignKey(Chat, on_delete=models.CASCADE, db_column='chatId',
                                     related_name='chatId')



