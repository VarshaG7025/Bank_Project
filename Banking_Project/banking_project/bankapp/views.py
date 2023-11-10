from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, CustomerForm

def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('customer_record')
        else:
            messages.error(request, "Login failed. Please check your username and password.")
    return render(request, 'home.html')


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have successfully registered! Welcome!')
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = CustomerForm.objects.get(id=pk)
        return render(request, 'customer_record.html', {'customer_record': customer_record})
    else:
        messages.success(request, 'You must be logged in to view that page...')
        return redirect('home')

def customer_record(request):
    form = CustomerForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                customer_record = form.save()
                messages.success(request,"Your Form Added Successfully")
                return redirect('home')
        return render(request,'customer_record.html',{'form':form})
    else:
        messages.success(request, "You Must Be Logged In..")
        return redirect('home')




