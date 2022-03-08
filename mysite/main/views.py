from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import ECGList,ECGdata
from .forms import CreateNewList
from django.contrib.sessions.models import Session

import threading
import os

# Create your views here.
def home(response):
    return render(response,"main/home.html",{"name":"test"})

def checkid(response, id = None):
    name = ECGList.objects.get(id=id)
    #name1 = ToDoList.objects.get(id=id)
    ls = ECGdata.objects.filter(ecgdata_id=id)
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
                a = ECGdata()
                a.ecglist = name
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
            t = ECGList(name=n)
            t.save()
            response.user.ecglist.add(t)
        return HttpResponseRedirect("/%i"%t.id)
    else:
        form = CreateNewList()       
    return render(response, "main/create.html",{"form":form})

def view(response):
    return render(response,"main/view.html",{})

def serverTest(response):
    # os.system("clear")
    # print("response: ",end="")
    # print(response)
    # from . import wstest
    #threading.Thread(target=wstest.echo()).start()
    # wstest.echo()
    return render(response,"main/serverTest.html",{})


def index(request):
    sid = request.COOKIES['sessionid']
    s = Session.objects.get(pk=sid)
    s_info = 'Session ID:' + sid + '<br>Expire_date:' + str(s.expire_date) + '<br>Data:' + str(s.get_decoded())
    return HttpResponse(s_info)