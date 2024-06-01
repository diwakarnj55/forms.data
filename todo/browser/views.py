from django.shortcuts import render,redirect
from . forms import TodoForm
def index(request):
    to=TodoForm()
    data ={
        "to":to,
    }
    if request.method=="POST":
        Todo=TodoForm(request.POST)
        if Todo .is_valid():
            Todo.save()
            return redirect("home")
    return render(request,"index.html",data)
