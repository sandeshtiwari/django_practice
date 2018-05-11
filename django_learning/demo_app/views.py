from django.shortcuts import render
from django.http import HttpResponse
from demo_app.models import AccessRecord, Topic, Webpage
# Create your views here.

def index(request):
    my_dict = {'insert_here': 'This is the value to be inserted in from the template tag'}
    return render(request, 'demo_app/index.html', context=my_dict)
def help(request):
    my_dict = {'help': 'The help page templage tag value'}
    return render(request, 'demo_app/help.html', context=my_dict)
def records(request):
    access_rec = AccessRecord.objects.order_by('date')
    dict = {'access_data':access_rec}
    return render(request, "demo_app/records.html", context=dict)
