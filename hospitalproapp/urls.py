
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('booking',views.booking,name='booking'),
    path('docter',views.docters,name='Docters'),
    path('contact',views.contact,name='contact'),
    path('department',views.department,name='Departments'),
]