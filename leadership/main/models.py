from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Header(models.Model):
    title = models.CharField('Header name: ', max_length=75)
    date = models.DateField('day',)
    date2 = models.IntegerField('Untill: ')
    
    
    video = models.FileField('Header video:', upload_to='media')
    now = timezone.now()
   
    img1 = models.ImageField('Img 1:',upload_to='media')
    title_img1 = models.CharField('Img 1 title: ', max_length=75)
    
    img2 = models.ImageField('Img 2:',upload_to='media')
    title_img2 = models.CharField('Img 2 title: ', max_length=75)

    img3 = models.ImageField('Img 3:',upload_to='media')
    title_img3 = models.CharField('Img 3 title: ', max_length=75)



    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = 'Header'
        verbose_name_plural = 'Header'



class About(models.Model):
    title1 = models.CharField('Title 1: ', max_length=75)
    title2 = models.CharField('Title 2 : ', max_length=75)
    title3 = models.CharField('Title 3 : ', max_length=75)

    txt = models.TextField('Text: ')
    def __str__(self) -> str:
        return self.title1
    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'

class AboutPhoto(models.Model):
    img = models.ImageField('Img :',upload_to='media')
    def __str__(self) -> str:
        return 'About photo'
    class Meta:
        verbose_name = 'About photo'
        verbose_name_plural = 'About photos'

class SpeakerTitile(models.Model):
    title = models.CharField('Title: ', max_length=75)
    txt = models.TextField('Text: ')
    name = models.CharField('Name: ', max_length=75)
    profesion = models.CharField('Profesion: ', max_length=75)
    img = models.ImageField('Img :',upload_to='media')
    facebook = models.URLField('Facebook: ',blank=True)
    instagram = models.URLField('Instagram :',blank=True)
    gmail = models.URLField('Gmail :',blank=True , null=True)
    whatsapp = models.URLField('Whatsapp :',blank=True , null=True)

    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = 'Speaker Titile'
        verbose_name_plural = 'Speaker Titiles'

class SpeakerInformation(models.Model):
    name = models.CharField('Name: ', max_length=75)
    profesion = models.CharField('Profesion: ', max_length=75)
    img = models.ImageField('Img :',upload_to='media')
    facebook = models.URLField('Facebook: ',blank=True)
    instagram = models.URLField('Instagram :',blank=True)
    gmail = models.URLField('Gmail :',blank=True , null=True)
    whatsapp = models.URLField('Whatsapp :',blank=True , null=True)

    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = 'Speaker Information'
        verbose_name_plural = 'Speaker Informations'
    


class SchedulesDays(models.Model):
    day = models.CharField('Day: ' ,max_length=70)
    date  =models.DateField('Date: ')
    def __str__(self) -> str:
        return self.day
    class Meta:
        verbose_name = 'Schedule Day'
        verbose_name_plural = 'Schedules Days'


class SchedulesInformation(models.Model):
    people = models.ForeignKey(SpeakerInformation,on_delete=models.CASCADE, related_name = 'people')
    category = models.ForeignKey(SchedulesDays, on_delete=models.CASCADE, related_name='schedules', null = True, blank=True)
    title = models.CharField('Title: ', max_length=75)
    txt = models.TextField('Text: ')
    name = models.CharField('Name: ', max_length=75,blank= True)
    place = models.CharField('Place: ', max_length=75)

    img = models.ImageField('Img :',upload_to='media')

    hour1  =models.TimeField('Hour 1: ')
    hour2  =models.TimeField('Hour 1: ')

    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = 'Schedule Information'
        verbose_name_plural = 'Schedules Informations'

class RegisterToday(models.Model):
    
    title = models.CharField('Title: ', max_length=75)
    txt = models.TextField('Text: ')
 
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = 'RegisterToday'
        verbose_name_plural = 'RegisterToday'


class PricingTitle(models.Model):
    
    title = models.CharField('Title: ', max_length=75)
    
 
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = 'Pricing title'
        verbose_name_plural = 'Pricings title'

class Pricing(models.Model):
    
    title = models.CharField('Title: ', max_length=75)
    price = models.IntegerField('Price: ')
    offer = models.CharField('Offer: ',max_length=75)
    place = models.CharField('Place : ',max_length=75)
    support = models.CharField('Support time : ', max_length=75)
    txt = models.TextField('Text :')
 
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = 'Pricing'
        verbose_name_plural = 'Pricings'

class Venue(models.Model):
    
    header = models.CharField('Header: ', max_length=75)
    title = models.CharField('Title: ', max_length=75)
    adress = models.CharField('Adress: ',max_length=255)
    email = models.EmailField('Email: ')

    phone = PhoneNumberField('Phone: ')

 
    def __str__(self) -> str:
        return self.header
    class Meta:
        verbose_name = 'Venue'
        verbose_name_plural = 'Venues'

class Message(models.Model):
    name = models.CharField('Name: ',max_length=75)
    email = models.EmailField('Email: ')
    subject = models.TextField('Subject: ')
    message = models.TextField('Subject: ')
    


    def __str__(self) -> str:
        return self.email
    
    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'



class FooterContact(models.Model):
    facebook = models.URLField('Facebook: ',blank=True)
    instagram = models.URLField('Instagram :',blank=True)
    youtube = models.URLField('YouTube :',blank=True , null=True)
    whatsapp = models.URLField('Whatsapp :',blank=True , null=True)
    def __str__(self) -> str:
        return 'email'
    
    class Meta:
        verbose_name = 'FooterContact'
        verbose_name_plural = 'FooterContact'
