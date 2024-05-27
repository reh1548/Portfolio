from django.shortcuts import render
from .models import Projects
import smtplib, ssl
import os
from dotenv import load_dotenv
load_dotenv()

my_mail = os.getenv("MY_MAIL")
password = os.getenv("MY_MAIL_PASSWORD")
recipient_mail = os.getenv("RECIPIENT_MAIL")


# Create your views here.
def index(request):
    return render(request, 'base/index.html')

def about(request):
    return render(request, 'base/about.html')


def message(msg):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(my_mail, password)
        server.sendmail(my_mail, recipient_mail, msg)

def contact(request):
    if request.method == 'POST':
        message(f"Subject: Portfolio Site Message\n\n{request.POST.get('name')}\n{request.POST.get('email')}\n\nMessage:{request.POST.get('message')}")
    return render(request, 'base/contact.html')


def projects(request):
    all_projects = Projects.objects.all()
    return render(request, 'base/projects.html', {'projects': all_projects})


