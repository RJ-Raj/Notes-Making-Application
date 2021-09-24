from django.core.checks import messages
from django.forms import widgets
from django.shortcuts import redirect, render
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from .models import *


# Create your views here.
def home(request):
    if request.method == "POST":
        title = request.POST.get('title')
        contents = request.POST.get('contents') or None
        due = request.POST.get('due_date') or None
        Todo.objects.create(title=title,content=contents,due=due)
    context = {"title":Todo.objects.all()}
    return render(request,'home.html',context)

def delete(request,id):
    try:
        todo_title = Todo.objects.get(id = id).delete()
    except Exception as e:
        messages.ERROR(request,"Cannot Delete")
    
    return redirect('/')

def update_doto(request):
    id = request.GET.get('id')
    try:
        todo_title = Todo.objects.get(id = id)
        todo_title.is_completed = not todo_title.is_completed
        todo_title.save()
    except Exception as e:
        messages.ERROR(request,"Cannot Delete")

    return redirect('/')


