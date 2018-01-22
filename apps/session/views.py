# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from time import localtime, strftime

def index(request):
    if not 'words' in request.session:
        request.session['words'] = []
    print request.session['words']
    context = {
        'words': request.session['words']
    }
    return render(request, "session/index.html", context)

def add_word(request):
    new_words = {
        'new_word': request.POST['new_word'],
        'color': request.POST['color'],
        'time': strftime("%b %d, %Y %H:%M %p", localtime())
    }
    if 'big_font' in request.POST:
        new_words['big_font'] = True
    else:
        new_words['big_font'] = False
    request.session['words'].append(new_words)
    request.session.modified = True
    return redirect('/')

def clear(request):
    del request.session['words']
    return redirect('/')
