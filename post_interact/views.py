from django.shortcuts import render, HttpResponse


def hello_message(request):
    return HttpResponse('Hello there!')
