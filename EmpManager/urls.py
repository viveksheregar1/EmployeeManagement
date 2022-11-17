from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('addemp',views.addemp,name="addemp"),
    path('searchemp',views.searchemp,name="searchemp"),
    path('employee',views.employee,name="employee"),


]