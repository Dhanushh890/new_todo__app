from django.http import HttpResponse
from django.shortcuts import render,redirect
from ToDo_app.models import ToDolist


def Task(request):
    ToDo_list=ToDolist.objects.all()

    return render(request,'index.html',{'items':ToDo_list})


def home(request):
    return render(request,'boat.html')


def Add_Task(request):
    if request.method=='POST':

        text=request.POST['text']
        s=ToDolist(text=text)
        s.save()
        return redirect('todo/')
    return render(request,'Add_Task.html')

def Delete(request,id):

    s=ToDolist.objects.get(id=id)
    s.delete()
    return redirect('Task')