from django.shortcuts import render, redirect
from admin_datta.forms import RegistrationForm, LoginForm, UserPasswordChangeForm, UserPasswordResetForm, UserSetPasswordForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetConfirmView, PasswordResetView
from django.views.generic import CreateView
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required

from .models import *



import pickle





def index(request):

  context = {
    'segment'  : 'index',
    #'products' : Product.objects.all()
  }
  return render(request, "pages/index.html", context)

def tables(request):
  context = {
    'segment': 'tables'
  }
  return render(request, "pages/dynamic-tables.html", context)




def form(request):
  return render(request, "includes/forms.html")





def formulaire(request):

    campaignName = request.GET.get('campaignName', '')
    budget = request.GET.get('budget', '')
    productType = request.GET.get('productType', '')
    targetAudience = request.GET.get('targetAudience', '')
    country = request.GET.get('country', '')
    platform = request.GET.get('platform', '')
    slogan = request.GET.get('slogan', '')
    campaignObjectives = request.GET.get('campaignObjectives', '')
    creativeAgency = request.GET.get('creativeAgency', '')
    colorPalette = request.GET.get('colorPalette', '')
    messagesTone = request.GET.get('messagesTone', '')
    startDate = request.GET.get('startDate', '')
    endDate = request.GET.get('endDate', '')
    



    # Load the pre-trained SVM model
    model1 = pickle.load('Hackaton.pkl')
    model2 = pickle.load('Efficiency.pkl')
    model3 = pickle.load('Profits.pkl')
    prediction1 = model1.predict(campaignName,budget,productType,targetAudience,country,platform,slogan,campaignObjectives,creativeAgency,colorPalette,messagesTone,startDate,endDate)
    prediction2 = model2.predict(campaignName,budget,productType,targetAudience,country,platform,slogan,campaignObjectives,creativeAgency,colorPalette,messagesTone,startDate,endDate)
    prediction3 = model3.predict(campaignName,budget,productType,targetAudience,country,platform,slogan,campaignObjectives,creativeAgency,colorPalette,messagesTone,startDate,endDate)
    
    print(prediction1)
    print(prediction2)
    print(prediction3)

    # Pass the mapped prediction value to the template context
    context = {'prediction': prediction1}
    # Pass the prediction value to the template context
    return render(request, "includes/sentiment.html", context)




