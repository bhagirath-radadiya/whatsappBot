''' model base whatsapp chatbot '''

from django.shortcuts import render, redirect
import requests
from rest_framework.renderers import JSONRenderer
from twilio.twiml.messaging_response import MessagingResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Chat, File
from .serializer import ChatSerializer, FileSerializer
import json
from django.http.response import JsonResponse
from django.core import serializers
from django.core.serializers.python import Serializer
from rest_framework.response import Response
import os


@csrf_exempt
def modelBot(request):
    if request.method == 'POST':

        print(">>> logs >>>", request.POST)

        if 'Body' in request.POST:
            incoming_msg = request.POST['Body'].lower()
        else:
            incoming_msg = None

        resp = MessagingResponse()

        ''' get model object '''
        char_object = Chat.objects.all()

        for i in char_object:
            incoming_list = i.incommingMsg.split("::")

            counter = 0
            if incoming_msg in incoming_list:

                reply_list = i.reply.split("::")

                ''' create dynamic variable for send message'''
                create_msg_obj = []
                create_txt_obj = []
                for reply in range(len(reply_list)):
                    create_msg_obj.append("msg" + str(reply))
                    create_txt_obj.append("txt" + str(reply))

                ''' text message '''
                for send in range(len(i.reply.split("::"))):
                    create_msg_obj[counter] = resp.message()
                    create_txt_obj[counter] = reply_list[counter]
                    create_msg_obj[counter].body(create_txt_obj[counter])
                    counter += 1

                # ''' image message '''
                # get_media_list = File.objects.filter(chatId_id=i.pk)
                # if len(get_media_list) > 0:
                #     create_msg_obj = []
                #     for msg in range(counter, counter + len(get_media_list)):
                #         create_msg_obj.append("msg" + str(msg))
                #
                #     create_img_obj = []
                #     for img in range(len(get_media_list)):
                #         create_img_obj.append("img" + str(img))
                #
                #     counter = 0
                #     for media in get_media_list:
                #         create_msg_obj[counter] = resp.message()
                #         create_msg_obj[counter].media(media.file.path)  # media compolsory on https
                #         counter += 1

                # ''' delete this path at hosting time this is only sample '''
                #
                # sample = ['https://bhagirath.imfast.io/res/0891bfd62aad63622588590f65458347.mp4',
                #           'https://bhagirath.imfast.io/res/1.jpg', 'https://bhagirath.imfast.io/res/ai%20sylabus.pdf']
                #
                # sample_counter = 0
                # create_msg_obj = ['msg100', 'msg101', 'msg102']
                #
                # for media in range(len(sample)):
                #     create_msg_obj[media] = resp.message()
                #     create_msg_obj[media].media(sample[media])
                #     sample_counter += 1
                #
                # ''' / delete end'''

                print(">>>> resp >>>>  ", resp)
        return HttpResponse(str(resp))


def view(request):
    chat = Chat.objects.all()
    chat_serializer = ChatSerializer(chat, many=True)

    x = JSONRenderer().render(chat_serializer.data)
    print(">>> x >>>", x)
    print(type(x))

    y = x.decode('utf-8')
    print(">>> y >>>", y)
    print(type(y))

    z = json.loads(x)
    print(">>> z >>>", z)
    print(type(z))

    return render(request, 'index.html', {'data': z})


def insert(request):
    incommingMessage = request.POST['incommingMessage']
    reply = request.POST['reply']
    file = request.FILES.getlist('file')

    createChat = Chat(incommingMsg=incommingMessage, reply=reply)
    createChat.save()

    for i in file:
        File(file=i, chatId_id=createChat.id).save()

    return redirect('/view')


def edit(request):
    id = request.GET['id']
    edit = Chat.objects.get(pk=id)

    chat = Chat.objects.all()
    chat_serializer = ChatSerializer(chat, many=True)

    x = JSONRenderer().render(chat_serializer.data)
    print(">>> x >>>", x)
    print(type(x))

    y = x.decode('utf-8')
    print(">>> y >>>", y)
    print(type(y))

    z = json.loads(x)
    print(">>> z >>>", z)
    print(type(z))

    return render(request, 'index.html', {'data': z, 'edit': edit})


def update(request):
    id = request.POST['id']
    incommingMessage = request.POST['incommingMessage']
    reply = request.POST['reply']
    file = request.FILES.getlist('file')

    update = Chat.objects.get(pk=id)
    update.incommingMsg = incommingMessage
    update.reply = reply

    for i in file:
        File(file=i, chatId_id=update.id).save()

    update.save()

    return redirect("/view")


def delete(request):
    id = request.GET['id']
    getChat = Chat.objects.get(pk=id)

    getFile = File.objects.filter(chatId_id=id)
    for i in getFile:
        file = i.file
        os.remove(file.path)

    getChat.delete()

    return redirect("/view")


def deleteFile(request):
    id = request.GET['id']
    getFile = File.objects.get(pk=id)

    file = getFile.file
    os.remove(file.path)

    getFile.delete()

    return redirect("/view")
