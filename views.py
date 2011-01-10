from django.template.loader import get_template
from django.template import Context, RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.cache import cache_page

from frankfeeds.models import Project, Snippet

from google.appengine.api import mail

@cache_page (60 * 15)
def home (request):
    contactmsg = ''
    contactfail = False
    if ('contact' in request.POST):
        if (request.POST['contact'] != 'Please type your message and contact details here.'):
            contactmsg = 'Thankyou for your message. I\'ll be in touch with you soon'
            sender_address = "contact@frankencode.appspotmail.com"
            reciever_address = "mark.doffman@gmail.com"
            subject = "Frankencode contact message : %s" % (request.POST['contact'][:20],)
            body = request.POST['contact']
            mail.send_mail(sender_address, reciever_address, subject, body)
        else:
            contactmsg = 'You didn\'t say anything. Please enter your message and try again.'
            contactfail = True

    try:
        about = Snippet.objects.get(name='about')
    except Snippet.DoesNotExist:
        about = ''

    return render_to_response ('home.html', context_instance=RequestContext(request, 
                                                            {'about':about,
                                                             'contactmsg':contactmsg,
                                                             'contactfail':contactfail}))

def hire (request):
    try:
        hire_me = Snippet.objects.get(name='hire-me')
    except Snippet.DoesNotExist:
        hire_me = ''
    return render_to_response ('hire.html', context_instance=RequestContext(request, {'hire_me':hire_me,}))

def projects (request):
    return render_to_response ('project.html', context_instance = RequestContext(request, {'projects': Project.objects.all(),}))

def resume (request):
    return render_to_response ('resume.html', context_instance = RequestContext(request, {'projects': Project.objects.all(),}))
