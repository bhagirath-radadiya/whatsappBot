''' static whatsapp chatbot '''

from django.shortcuts import render
import requests
from twilio.twiml.messaging_response import MessagingResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


@csrf_exempt
def mybot(request):
    if request.method == 'POST':
        incoming_msg = request.POST['Body']
        incoming_msg = incoming_msg.lower()

        resp = MessagingResponse()

        if incoming_msg in ['hi', 'hii', 'hello', 'hey']:
            msg1 = resp.message()
            txt1 = '''Hi Welcome to SOLK NETWORK. 👋'''
            msg1.body(txt1)

            msg2 = resp.message()
            txt2 = '''I am *SOLK* bot'''
            msg2.body(txt2)

            msg3 = resp.message()
            txt3 = '''please select  bellow options.
About
Services
Technology
Solutions
Work'''
            msg3.body(txt3)


        elif incoming_msg in ['home']:
            msg1 = resp.message()
            response = '''*Home*

please select  bellow options.

About
Services
Technology
Solutions'''
            msg1.body(response)

        elif incoming_msg in ['about']:
            msg1 = resp.message()
            response = '''*About Us*

SOLK NETWORK is not only a globally recognized IT company but also a family filled with talented experts that help global brands, enterprises, mid-size businesses or even startups with innovative solutions.

We've helped businesses increase their revenue on an average by 90% in their first year with us!
*3000+* Satisfied Clients Across the Globe
*7000+* Projects Delivered Successfully
*450+* Experts Under the Same Roof

“To live life within boundaries, to limit your existence by fearing the unexpected, to make choices based on needs and not wants, that is humanity’s biggest failure.”'''
            msg1.body(response)

        elif incoming_msg in ['services']:
            msg1 = resp.message()
            response = '''*Services*

Mobile Apps Development
Web Development
UI/UX Design
IoT Solutions
Wearables App Development
AI - ML App Development
Quality Assurance (QA)
Hire Dedicated Developers
Virtual Reality Apps Development
Mobile Game Development
Home'''
            msg1.body(response)
            msg1.media('https://bhagirath.imfast.io/res/images/blog-1.jpg')

        elif incoming_msg in ['technology']:
            msg1 = resp.message()
            response = '''*Technology*

Mobile
Backend
Frontend
Infra and DevOps
Database
CMS
Home'''
            msg1.body(response)

            msg2 = resp.message()
            msg2.media('https://blog.mozilla.org/security/files/2015/05/HTTPS-FAQ.pdf')
            msg2.body(response)

        elif incoming_msg in ['solutions']:
            msg1 = resp.message()
            msg1.media('https://bhagirath.imfast.io/res/video/homevideo.mp4')
            response = '''*Solutions*

Enterprise
B2B
B2C
Home'''
            msg1.body(response)

        else:
            msg1 = resp.message()
            msg1.body('આ પ્રકાર ની કોઈ આઇટમ નથી')

        return HttpResponse(str(resp))
