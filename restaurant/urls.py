from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("form.html",views.home,name="home"),
    path("super",views.ins_upd_del,name="insert"),
    path("menu.html",views.disp,name="menu")
]