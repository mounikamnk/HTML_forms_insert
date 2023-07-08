from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def first(request):
    if request.method=='POST':
        username=request.POST['un']
        password=request.POST['pw']
        print(username)
        print(password)
        return HttpResponse('data is submited')
    return render(request,'first.html')

def insert_topic(request):
    if request.method=='POST':
        topic=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=topic)[0]
        TO.save()
        return HttpResponse('insertion of topic is done')

    return render(request,'insert_topic.html')


def insert_webpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        topic=request.POST['tn']
        TO=Topic.objects.get(topic_name=topic)
        name=request.POST['name']
        url=request.POST['url']
        WO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url)[0]
        WO.save()
        return HttpResponse('insertion of webpage is done')
    return render(request,'insert_webpage.html',d)

def insert_accessrecord(request):
    if request.method=='POST':
        name=request.POST['name']
        WO=Webpage.objects.get(name=name)
        date=request.POST['date']
        author=request.POST['author']
        AO=AccessRecord.objects.get_or_create(name=WO,date=date,author=author)[0]
        AO.save()
        return HttpResponse('insertion of accessrecord is done')
    return render(request,'insert_accessrecord.html')


