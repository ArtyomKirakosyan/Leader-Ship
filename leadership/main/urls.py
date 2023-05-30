from django.urls import path
from . views import *



urlpatterns = [
   path('', HomeListView.as_view(), name = 'home'),
   path('register/',RegisterPage,name='register'),
   path('login/',LoginPage,name='login'),
   path('logout_request/', logout_request, name = 'logout'),

]