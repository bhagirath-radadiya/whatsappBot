''' send whatsapp message using json '''


from django.shortcuts import render
from twilio.twiml.messaging_response import MessagingResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.

data = {'0': {'txt': 'Hi Welcome to *SOLK NETWORK*. 👋'},
        '1': {'file': 'https://bhagirath.imfast.io/res/1.jpg'},
        '2': {'txt': 'I am *SOLK* bot'},
        '3': {'file': 'https://bhagirath.imfast.io/res/0891bfd62aad63622588590f65458347.mp4'},
        '4': {'txt': '''please select  bellow options.
About
Services
Technology
Solutions
Work'''},
        '5': {'file': 'https://bhagirath.imfast.io/res/ai%20sylabus.pdf'}}


@csrf_exempt
def alternate(request):
    incoming_msg = request.POST['Body']
    incoming_msg = incoming_msg.lower()
    resp = MessagingResponse()

    create_msg_obj = []
    for i in range(len(data)):
        create_msg_obj.append('msg' + str(i))

    for i in range(len(data)):
        create_msg_obj[i] = resp.message()

        varify = data[str(i)]
        if list(varify.keys())[0] == 'txt':
            create_msg_obj[i].body(data[str(i)]['txt'])

        if list(varify.keys())[0] == 'file':
            create_msg_obj[i].media(data[str(i)]['file'])

    return HttpResponse(str(resp))
