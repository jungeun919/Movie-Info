from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    return render(request, 'index.html')

def sendEmail(request):
    inputReceiver = request.POST['inputReceiver']
    inputTitle = request.POST['inputTitle']
    inputContent = request.POST['inputContent']

    content = {'inputReceiver':inputReceiver, 'inputTitle':inputTitle, 'inputContent':inputContent}
    
    msg_html = render_to_string('email_format.html', content)

    msg = EmailMessage(subject=inputTitle, body=msg_html, from_email="djangoemailtester001@gmail.com", bcc=inputReceiver.split(','))
    msg.content_subtype = 'html'
    msg.send()
    return HttpResponseRedirect(reverse('index'))