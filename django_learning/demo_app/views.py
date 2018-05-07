from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {'insert_here': 'This is the value to be inserted in from the template tag'}
    return render(request, 'demo_app/index.html', context=my_dict)
def help(request):
    my_dict = {'help': 'The help page templage tag value'}
    return render(request, 'demo_app/help.html', context=my_dict)
