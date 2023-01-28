from django.shortcuts import render
from app.models import *
# Create your views here.
from app.views import *
from django.db.models import Q

def display_topics(request):
    QST=Topic.objects.all()
    QST=Topic.objects.filter(topic_name='cricket')
    d={'topics':QST}
    return render(request,'display_topics.html',d)

def display_Webpage(request):
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(topic_name='cricket')
    QSW=Webpage.objects.exclude(topic_name='cricket')
    QSW=Webpage.objects.all()[:5:]
    QSW=Webpage.objects.all().order_by('name')
    QSW=Webpage.objects.all().order_by('-name')
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(Url__startswith='https')
    QSW=Webpage.objects.filter(Url__startswith='http')
    QSW=Webpage.objects.filter(name__startswith='s')
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(name__contains='s')
    QSW=Webpage.objects.filter(name__regex='\w{5}')
    QSW=Webpage.objects.filter(name__in=['sai','vani','mammu'])
    QSW=Webpage.objects.filter(Q(topic_name='cricket') | Q(name='sai'))
    QSW=Webpage.objects.all()
   

    d={'Webpage':QSW}
    return render(request,'display_Webpage.html',d)
    
def display_accessrecord(request):
    QSA=AccessRecords.objects.all()
    QSA=Webpage.objects.all().order_by('name')
    QSA=Webpage.objects.all()
    QSA=AccessRecords.objects.filter(date='1998-8-10')
    QSA=AccessRecords.objects.filter(date__gt='1998-8-10')
    QSA=AccessRecords.objects.filter(date__gte='1998-8-10')
    QSA=AccessRecords.objects.filter(date__lt='2000-8-10')
    QSA=AccessRecords.objects.filter(date__lte='1998-8-10')
    QSA=AccessRecords.objects.filter(date__year='1998')
    QSA=AccessRecords.objects.filter(date__month='10')
    QSA=AccessRecords.objects.filter(date__day='11')
    
    

    d={'AccessRecords':QSA}
    return render(request,'display_access.html',d)

def update_Webpage(request):
    Webpage.objects.filter(name='vani').update(Url='http://vani.in')  
    Webpage.objects.filter(name='vani').update(topic_name='tennis')
    Webpage.objects.filter(topic_name='tennis') .update(name='sindhu')
    Webpage.objects.update_or_create(name='sindhu',defaults={'Url':'http://sindhu.com'})                                                                                   
    QSW=Webpage.objects.all()
    d={'Webpage':QSW}
    return render(request,'display_Webpage.html',d)
    
