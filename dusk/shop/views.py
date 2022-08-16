from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('This is homepage.')

def about(request):
    return HttpResponse('This is about page.')
