from django.contrib import messages
import os.path
from django.contrib.auth import login
from django.contrib.auth import authenticate, login
from django.http import JsonResponse, HttpResponse
from django.shortcuts import  get_object_or_404
from django_daraja.mpesa.core import MpesaClient
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import radicalConnect

from radicalConnect import forms
from radicalConnect.Serializers import ContactSerializer
from radicalConnect.forms import ContactForm, AccountForm,FutureSkillForm,UserLoginForm
from radicalConnect.models import Contact
from django.shortcuts import render, redirect




def about(request):
    data = Contact.objects.all()
    context = {'data': data}
    return render(request, 'about.html',context)
def about0(request):
    return render(request, 'about0.html')
def contact(request):
    if request.method == "POST":
     form = ContactForm(request.POST,request.FILES)
     if form.is_valid():
        form.save()
        return redirect('about')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def blog(request):
    return render(request, 'blog.html')
def base(request):
    return render(request, 'base.html')




def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('https://openstax.org/')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = UserLoginForm()
    return render(request, 'login_view.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form2 = AccountForm(request.POST)
        if form2.is_valid():
            form2.save()
            return redirect('login_view')
    else:
        form2 = AccountForm()
    return render(request, 'signup.html',{'form2': form2} )


def index(request):
    if request.method == 'POST':
        form3 = FutureSkillForm(request.POST)
        if form3.is_valid():
            form3.save()
        return redirect('index')
    else:
        form3 = FutureSkillForm()
    return render(request, 'index.html',{'form3': form3})


def update(request, id,):
    radicalConnect = get_object_or_404(Contact, id=id)
    if request.method == "POST":
        form4= ContactForm(request.POST, request.FILES, instance=radicalConnect)
        if form4.is_valid():
            form4.save()
            if 'image' in request.FILES:
                file_name = os.path.basename(request.FILES['image'].name)
                messages.success(request, f'User updated successfully! {file_name} uploaded')
            else:
                messages.error(request, f'User updated successfully!')
                return redirect('about')
        else:
            messages.error(request, f'Please confirm your changes!')
    else:
        form4 = ContactForm(instance=radicalConnect)
    #find record by id ,update it,save it to db
    return render(request, 'update.html',{'form4': form4})



def delete(request, id):
    radicalConnect = get_object_or_404(Contact, id=id)

    try:
        radicalConnect.delete()
        messages.success(request, 'User deleted successfully!')
    except Exception as e:
        messages.error(request, 'User not deleted')
    return redirect('about')

@api_view(['GET','POST'])
def usersapi(request):
    if request.method == 'GET':
        users = Contact.objects.all()
        serializer = ContactSerializer(users, many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,safe=False,status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
def mpesa(request):
    client = MpesaClient()
    phoneNumber = '0717474393'
    amount = 1
    account_reference = 'Grace Onyango'
    transaction_desc = 'Payment for a radicalConnect course'
    callback_url = 'https://darajambili.herokuapp.com/callback'
    response = client.stk_push(phoneNumber, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse({'response': response})


def course(request):
    return render(request, 'course.html')