from django.shortcuts import render,redirect
from .forms import Todocreation,RegistrationForm,LoginForm
from .models import Todo
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    return render(request,"home.html")

def create_todo(request):
    context = {}
    form=Todocreation()
    context["form"]=form

    if request.method == "POST":
        form = Todocreation(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            context["form"] = form
            return render(request, "todocreate.html", context)
    return render(request, "todocreate.html", context)

def listtodo(request):
    todos=Todo.objects.all()
    context={}
    context["todos"]=todos
    return render(request,"listtodo.html",context)

def viewtodo(request,id):
    todo=Todo.objects.get(id=id)
    context={}
    context["todo"]=todo
    return render(request,"viewtodo.html",context)

def removetodo(request,id):
    todo=Todo.objects.get(id=id)
    todo.delete()
    return redirect("todolist")
def updatetodo(request,id):
    todo=Todo.objects.get(id=id)
    form=Todocreation(instance=todo)
    context={}
    context["form"]=form
    if request.method=="POST":
        form = Todocreation(instance=todo, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("todolist")

    return render(request,"updatetodo.html",context)

#registration and login

def registration_user(request):
    form=RegistrationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
        else:
            context["form"]=form
            return render(request,"registration.html",context)

    return render(request, "registration.html", context)

def signin(request):
    form=LoginForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect("home")
            else:
                context["form"]=form
                return render(request,"login.html",context)
    return render(request, "login.html", context)

def signout(request):
    logout(request)
    return redirect("signin")