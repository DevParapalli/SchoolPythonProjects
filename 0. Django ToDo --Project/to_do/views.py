from django.shortcuts import render, redirect
from django.urls import reverse

from .models import ToDo
from .forms import ToDoForm
# Create your views here.
def to_do(request):
    reminder_list = ToDo.objects.order_by('-dead_line')
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('to_do')
    form = ToDoForm()
    
    navbar_list = [
        {
            'link':reverse('index'),
            'name':'HOME'
        },
        {
            'link':reverse('to_do'),
            'name':'TO-DO'
        }
    ]
    
    
    
    if len(reminder_list) == 0:
        reminder_list = [
            {
                "title":'No Reminders Here.',
                "data":"Start by creating one above.",
                "created_date_time":"",
                "dead_line":""
            }
        ]
    
    context = {
        'page_title':'To-Do By RogueCatalyst',
        'nav_bar':navbar_list,
        'content':{},
        'form':form.as_table(),
        'to_do_list':reminder_list,
        
    }
    
    
    return render(request, 'to_do/to_do.html', context=context)

def remove(request, identifier):
    item = ToDo.objects.get(id=identifier) 
    item.delete() 
    return redirect('to_do')


def index(request):
    
    content_list = [
        {
            'number':'one',
            'title':'Test for TO-DO App',
            'style':'style1',
            'image':'/images/pic01.jpg', # this is the picture used for the content. change a/c to context
            'alt_image':'Just a gradient used in development.',
            'link': reverse('to_do'),
            'link_text':'TO-DO',
            'content':'The to_do page calls you.'
        },
        {
            'number':'two',
            ''
            'title':'This is Solid State',
            'style':'alt style2', # alt should be alternately inserted into style for criss cross patterns
            'image':'/images/pic02.jpg', # this is the picture used for the content. change a/c to context
            'alt_image':'Just a gradient used in development.',
            'link': reverse('index'),
            'link_text':'LEARN MORE',
            'content':'Another free + fully responsive site template by HTML5 UP (See Nav Bar for Details.)'
        }
    ]
    navbar_list = [
        {
            'link':reverse('index'),
            'name':'HOME'
        },
        {
            'link':reverse('to_do'),
            'name':'TO-DO'
        },
        {
            'link':"https://html5up.net/solid-state",
            'name':'TEMPLATE Details'
        }
    ]
    
    
    
    context = {
        'page_title':'RogueCatalyst',
        'nav_bar':navbar_list,
        'content':content_list,
    }
    return render(request, 'to_do/index.html', context)