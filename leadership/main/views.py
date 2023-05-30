from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from . models import *
from . form import *
from django.urls import re_path
from django.core.mail import EmailMessage
from leadership.settings import EMAIL_HOST_USER
from django.contrib.auth import authenticate,login,logout

class HomeListView(ListView):
    template_name='index.html'
    def get(self, request) :
        header = Header.objects.get()
        about = About.objects.get()
        about_photo = AboutPhoto.objects.all()
        speaker_title = SpeakerTitile.objects.get()
        speaker_information = SpeakerInformation.objects.all()
        schedules_days=SchedulesDays.objects.filter(id__in=[2,3,4])
        schedules_days_active=SchedulesDays.objects.filter(id=1)
        register_today=RegisterToday.objects.get()
        pricing_title=PricingTitle.objects.get()
        pricing = Pricing.objects.all()
        venue=Venue.objects.get()
        footer_contact=FooterContact.objects.get()

        form = MessageModelForm

        


        mod = {
            'header':header,
            'about': about,
            'about_photo': about_photo,
            'speaker_information': speaker_information,
            'speaker_title':speaker_title,
            'schedules_days':schedules_days,
            'schedules_days_active':schedules_days_active,
            'register_today':register_today,
            'pricing_title':pricing_title,
            'pricing':pricing,
            'venue':venue,
            'form':form,
            'footer_contact':footer_contact


        }
        return render(request, self.template_name,mod)
    def post(self,request):
        header = Header.objects.get()
        about = About.objects.get()
        about_photo = AboutPhoto.objects.all()
        speaker_title = SpeakerTitile.objects.get()
        speaker_information = SpeakerInformation.objects.all()
        schedules_days=SchedulesDays.objects.filter(id__in=[2,3,4])
        schedules_days_active=SchedulesDays.objects.first()
        register_today=RegisterToday.objects.get()
        pricing_title=PricingTitle.objects.get()
        pricing = Pricing.objects.all()
        footer_contact=FooterContact.objects.get()

        venue=Venue.objects.get()
       
       
        form = MessageModelForm()
        subject = f"Նոր Նամակ LeaderShip - ից"

        body = 'Ձեր կարծիքը կարևոր է մեզ համար'
        try:
            email = EmailMessage(
            subject = subject,
            body = body,
            from_email=EMAIL_HOST_USER,
            to=[request.POST.get('email')],
            )
            email.send()
        except Exception:
            pass
        

        
        form = MessageModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
            
        else:
            form = MessageModelForm()
                
                
        return render(request, self.template_name, {
            'form':form,
            'header':header,
            'about': about,
            'about_photo': about_photo,
            'speaker_information': speaker_information,
            'speaker_title':speaker_title,
            'schedules_days':schedules_days,
            'schedules_days_active':schedules_days_active,
            'register_today':register_today,
            'pricing_title':pricing_title,
            'pricing':pricing,
            'venue':venue,
            'footer_contact':footer_contact
            
            
        })
        

def RegisterPage(request):
    form=Create()
    if request.method=="POST":
        form=Create(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form=Create()

    return render(request,'register.html',{'form':form})




def LoginPage(request):
    template_name='login.html'

    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('register')

    return render(request,template_name)


def logout_request(request):
	logout(request)
	return redirect("home")
