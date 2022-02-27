from django.urls import path
from . import views

urlpatterns = [
    path("",views.home),
    path("home/",views.home),
    path("<int:id>/",views.checkid),                                                                                                
    path("create/",views.create),
    path("view/",views.view),
    path("serverTest",views.serverTest)
]
