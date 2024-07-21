"""
URL configuration for web_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from signup.views import signaction
from login.views import loginaction
from index.views import index 
from index.views import services 
from index.views import services_welcome 
from index.views import about_welcome 
from index.views import articles_welcome 
from index.views import articles
from index.views import about
from index.views import diet
from index.views import immune
from index.views import kidney
from index.views import lungs
from index.views import getstarted
from index.views import logo
from index.views import physical
from index.views import heart
from index.views import login
from index.views import signup
from index.views import welcome
from index.views import lab_locator
from index.views import med_locator
from index.views import search_results
from index.views import appointments
from django.views.generic import TemplateView
from index.views import labgui
from searchS import views
from index.views import dashboard
from index.views import medicines
from index.views import appointment_success

from django.conf import settings
from django.conf.urls.static import static

from searchS.views import autocomplete_search
from searchS.views import auto_search

from adminlogin.views import admin_login

from feedback.views import submit_feedback
from feedback2.views import submit_feedback

from appointments.views import submit_appointment
from appointments.views import get_appointments
from appointments.views import display
from appointments.views import accept_appointment
from appointments.views import reject_appointment
from appointments.views import add_medicine
from appointments.views import delete_medicine
from appointments.views import edit_medicine
from appointments.views import add_lab
from appointments.views import delete_lab
from appointments.views import edit_hospital



urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signaction, name='signaction'),
    path('login/',loginaction, name='loginaction'),
    path('', index, name='index'),
    path('services/', services, name='services'),
    path('services_welcome/', services_welcome, name='services_welcome'),
    path('about_welcome/', about_welcome, name='about_welcome'),
    path('articles_welcome/', articles_welcome, name='articles_welcome'),
    path('articles/', articles, name='articles'),
    path('about/', about, name='about'),
    path('diet/', diet, name='diet'),
    path('immune/', immune, name='immune'),
    path('kidney/', kidney, name='kidney'),
    path('getstarted/', getstarted, name='getstarted'),
    path('lungs/', lungs, name='lungs'),
    path('logo/', logo, name='logo'),
    path('physical/', physical, name='physical'),
    path('heart/', heart, name='heart'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('lab_locator/', lab_locator, name='lab_locator'),
    path('med_locator/', med_locator, name='med_locator'),
    path('welcome/', welcome, name='welcome'),
    path('search_results/', views.search_results, name='search_results'),
    # path('labgui/', views.search_result, name='labgui'),
    path('dashboard/', dashboard, name='dashboard'),
    path('med_results/', views.med_results, name='med_results'),
    path('autocomplete/', autocomplete_search, name='autocomplete_search'),
    path('auto/', auto_search, name='auto_search'),    
    path('appointments.html', appointments, name='appointments'),
    path('submit_appointment/', submit_appointment, name='submit_appointment'),
    path('appointment_success/', appointment_success, name='appointment_success'),
    path('get_appointments/', get_appointments, name='get_appointments'),
    path('dashboard.html/', get_appointments, name='display'),  #according to this url when the url in the browswer is empty then get_appointments function runs
    path('accept_appointment/<int:appointment_id>/', accept_appointment, name='accept_appointment'),
    path('reject_appointment/<int:appointment_id>/', reject_appointment, name='reject_appointment'),
    path('add_medicine/', add_medicine, name='add_medicine'),
    path('delete_medicine/<int:medicine_id>/', delete_medicine, name='delete_medicine'),
    path('edit_medicine/<int:medicine_id>/', edit_medicine, name='edit_medicine'),
    path('add_lab/', add_lab, name='add_lab'),
    path('delete_lab/<int:lab_id>/', delete_lab, name='delete_lab'),
    path('edit_hospital/<int:lab_id>/', edit_hospital, name='edit_hospital'),
    path('admin_login/', admin_login, name='admin_login'),
    path('submit_feedback/', submit_feedback, name='submit_feedback'),
    path('submit_feedback/', submit_feedback, name='submit_feedback'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)