from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import ToDoList,Item
from .forms import CreateNewList

# Create your views here.
def home(response):
    return render(response,"main/home.html",{"name":"test"})

def checkid(response, id = None):
    name = ToDoList.objects.get(id=id)
    #name1 = ToDoList.objects.get(id=id)
    ls = Item.objects.filter(todolist_id=id)
    #print(ls)
    #{"save":["save"]}
    if response.method == "POST":
        if response.POST.get("save"):
            for item in ls:
                if response.POST.get("c"+ str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()
        elif response.POST.get("newItem"):
            txt = response.POST.get("new")

            if len(txt) > 2:
                #print(type(name1))
                #print(type(ls))
                a = Item()
                a.todolist = name
                a.text = txt
                a.complete = False
                a.save()               
                return redirect(response.path,{"ls": ls, "name": name})
                #ls.item_set.create(text = txt, complete=False)
            else:
                print("invaild")
    return render(response,"main/list.html",{"ls": ls, "name": name})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)
        return HttpResponseRedirect("/%i"%t.id)
    else:
        form = CreateNewList()       
    return render(response, "main/create.html",{"form":form})

def view(response):
    return render(response,"main/view.html",{})

def serverTest(response):
    return render(response,"main/serverTest.html",{})