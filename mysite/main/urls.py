from django.urls import path
from . import views

from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path("",views.home),
    path("home/",views.home),
    path("<int:id>/",views.checkid),                                                                                                
    path("create/",views.create),
    path("view/",views.view),
    path("serverTest",views.serverTest),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('mysite/main/static/main/favicon.ico'))),
    path('index/', views.index)  
]
