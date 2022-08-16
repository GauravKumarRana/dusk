from django.shortcuts import render, HttpResponse

def index(request):
    context = { 'variable' : 'this is variable message'} # this is a python dictionary
    return render(request, 'index.html', context)
    # return HttpResponse('This is homepage.')

def about(request):
    return HttpResponse('This is about page.')

def services(request):
    return HttpResponse('This is services page.')

def contact(request):
    return HttpResponse('This is contact page.')
