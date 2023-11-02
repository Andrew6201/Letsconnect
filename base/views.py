from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Profile
from django.db.models import Q
from django.shortcuts import get_object_or_404


# Create your views here.
#my home page
def home(request):
    
    return render(request,'home.html')

#body of my page
def body(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    details = Profile.objects.filter(
        Q(job__icontains=q )|
        Q(country__icontains=q)|
        Q(state__icontains=q)|
        Q(description__icontains=q)
        )

    detail_count = details.count()
    profiledata = Profile.objects.filter(user=request.user)
    context = {"profiledata":profiledata, "details":details, "detail_count":detail_count}




      


    return render(request,'body.html',context)

def specificprofile(request,pk):
    details = Profile.objects.get(pk=pk)
    context = {"details":details}
    return render(request,'specificprofile.html',context)
#my navigation bar
def navbar(request):
    return render(request,'navbar.html')



#Registration logic
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists')
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')


        else:
            messages.info(request, "Password does not match")
            return redirect('register')
    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('body')
        else:
            messages.info(request,'Invalid credentials, try again!!')
            return redirect('login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def create_profile(request):
    if request.method == 'POST':
        
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        gender = request.POST['gender']
        country = request.POST['country']
        state = request.POST['state']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        job = request.POST['job']
        description = request.POST['description']
        user=request.user

        profile = Profile(user=user,firstname=firstname, lastname=lastname, gender=gender, country=country, state=state, email=email, phonenumber=phonenumber,job=job,description=description)
        profile.save()
        return redirect('body')


    return render(request,'create_profile.html')

def updateprofile(request,pk):
    profile = get_object_or_404(Profile, pk=pk)

    if request.method == 'POST':
        # Update the profile fields based on the POST data
        profile.firstname = request.POST['firstname']
        profile.lastname = request.POST['lastname']
        profile.gender = request.POST['gender']
        profile.country = request.POST['country']
        profile.state = request.POST['state']
        profile.email = request.POST['email']
        profile.phonenumber = request.POST['phonenumber']
        profile.job = request.POST['job']
        profile.description = request.POST['description']
        
        # Save the updated profile
        profile.save()

        return redirect('body')

    context = {'profile': profile}
    return render(request, 'updateprofile.html', context)