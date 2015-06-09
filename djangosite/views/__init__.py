__author__ = 'mark'
from django.http import Http404
from django.shortcuts import render_to_response
import datetime


def home(request):
    now = datetime.datetime.now()
    html = "It is now %s." % now
    return render_to_response('../templates/home.html', {"html": html})