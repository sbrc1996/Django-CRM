from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm,AddRecordForm
from .models import Record

# Create your views here.

#Our Home page will be our Login Page

def home(request):  
    records = Record.objects.all()      #Get everything in the table.

    #check to see if loggin in successful
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        #We got the username and the password entered by the user from the frontend and now authenticate
        # from the backend
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Successful login!!")
            return redirect('home')
        else:
            messages.error(request,"Login Unsuccessful!!")
            return redirect('home')
    else:
        return render(request,'home.html',{'records':records})


def logout_user(request):
    logout(request)
    messages.success(request,"Successfully Logged Out!!")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':        #if the user has entered data and submiited the form i.e Posting data
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and Login..
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username='username',password='password')
            login(request,user)
            messages.success(request,"Successfully registered and Logged In!!")
            return redirect('home')
    else:                           #The user has not entered any data and is clicked on the button, redirect to the same page with the django form.
        form = SignUpForm()
        return render(request,'register.html',{'form':form})
    return render(request,'register.html',{'form':form})


def customer_record(request,pk):
    if request.user.is_authenticated:
        #Retrieve the individual record
        customer_record = Record.objects.get(id=pk)
        return render(request,'record.html',{'customer_record':customer_record})
    else:
        messages.success(request,"You must be logged in to view that page!!")
        return redirect('home')


def delete_record(request,pk):
    if request.user.is_authenticated:
        #delete from the DB
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request,"record successfully deleted!!")
        return redirect('home')
    else:
        messages.success(request,"You must be logged in to delete the record !!")
        return redirect('home')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request,"Added Successfully!!")
                return redirect('home')     #After addition send it to home page
        return render(request,'add_record.html',{'form':form})      #Agar add nahi kiya toh wahi pe rakho
    else:
        messages.success(request,"You must be logged in to delete the record !!")
        return redirect('home')      
    


def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')

    
                

