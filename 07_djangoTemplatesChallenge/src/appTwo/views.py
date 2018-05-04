from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(doreviateam):
    message = "<em>My Second App</em>"
    return HttpResponse(message)


def help(request):
    template = 'appTwo/help.html'
    ctx = {
        'message': 'This is the help page'
    }

    return render(request, template_name=template, context=ctx)
