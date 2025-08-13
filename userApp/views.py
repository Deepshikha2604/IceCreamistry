from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from .models import profile 
from django.shortcuts import redirect
from django.contrib import messages
from .forms import SignUpForm, EditUserProfileForm, EditAdminProfileForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User

def profiles(request):
    pro=profile.objects.all()
    context={'pro':pro}
    return render(request, 'users/Profile.html',context)

def sign_up(request):
    print('Hello')
    print(request)
    if request.method == "GET":
        fm = SignUpForm(request.GET)
        print('Hello 2')
        if fm.is_valid():
            user=fm.save(commit=False)
            user.save()
            messages.success(request, 'Account created successfully')
            login(request,user)
            return redirect('profile')
    else:
        print('Else Hello')
        fm = SignUpForm()
        # print(fm)
    return render(request, 'users/signup.html', {'form': fm})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                user_name = fm.cleaned_data['username']
                user_password = fm.cleaned_data['password']
                user = authenticate(username=user_name, password=user_password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully !!')
                    return redirect('profile')
        else:
            fm = AuthenticationForm()
        return render(request, 'users/login.html', {'form': fm})
    else:
        return redirect('profile')

def user_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(request.POST, instance=request.user)
                users = User.objects.all()
            else:
                fm = EditUserProfileForm(request.POST, instance=request.user)
                users = None
            if fm.is_valid():
                messages.success(request, 'Profile updated')
                fm.save()
        else:
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(instance=request.user)
                users = User.objects.all()
            else:
                fm = EditUserProfileForm(instance=request.user)
                users = None
        return render(request, 'users/Profile.html', 
            {'name': request.user.username, 'form': fm, 'users': users})
    else:
        return redirect('login')

def user_logout(request):
    logout(request)
    return redirect('login')

# Change password with old password
def user_change_password(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                # Update user session
                update_session_auth_hash(request, fm.user)
                messages.success(request, 'Password changed successfully')
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request, 'users/changePassword.html', {'form': fm})
    else:
        return redirect('login')

# Change password without old password
def user_change_password2(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = SetPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                # Update user session
                update_session_auth_hash(request, fm.user)
                messages.success(request, 'Password changed successfully')
                return HttpResponseRedirect('/profile/')
        else:
            fm = SetPasswordForm(user=request.user)
        return render(request, 'users/changePassword2.html', {'form': fm})
    else:
        return redirect('login')

def user_detail(request, id):
    if request.user.is_authenticated:
        pi = User.objects.get(pk=id)
        fm = EditAdminProfileForm(instance=pi)
        return render(request, 'users/userdetail.html', 
            {'name': request.user.username,'form': fm})
    else:
        return redirect('login')

# Create your views here.
