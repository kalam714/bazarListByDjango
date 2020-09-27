from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from .forms import BazarForm
from .models import Bazar
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'bazar/home.html')




def signupuser(request):
    if request.method =="GET":
        return render(request, 'bazar/signupuser.html', {'form': UserCreationForm()})

    else:
        if request.POST['password1'] == request.POST['password2']:
            try:

                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currentList')
            except IntegrityError:
                return render(request, 'bazar/signupuser.html', {'form': UserCreationForm(), 'error': 'username already taken.try new one'})
        else:
            return render(request, 'bazar/signupuser.html', {'form': UserCreationForm(), 'error': 'password does not match'})



def loginuser(request):
    if request.method =="GET":
        return render(request, 'bazar/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request,'bazar/loginuser.html', {'form': AuthenticationForm(), 'error':'username or password does not match'})
        else:
            login(request, user)
            return redirect('currentList')





@login_required
def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')







@login_required
def list(request):
    if request.method =="GET":
        return render(request, 'bazar/list.html', {'form': BazarForm()})
    else:
        try:
            form = BazarForm(request.POST)
            newBazar = form.save(commit=False)
            newBazar.user = request.user
            newBazar.save()
            return redirect('currentList')
        except ValueError:
            return render(request, 'bazar/list.html', {'form': BazarForm(), 'error': 'Bad data'})



@login_required
def currentList(request):
    bazars = Bazar.objects.filter(user=request.user)

    return render(request, 'bazar/currentList.html', {'bazars':bazars})
@login_required
def viewBazar(request, bazar_pk):
    bazar = get_object_or_404(Bazar, pk=bazar_pk, user=request.user)
    if request.method == "GET":
        form=BazarForm(instance=bazar)
        return render(request, 'bazar/viewlist.html', {'bazar': bazar, 'form':form})
    else:
        try:
            form = BazarForm(request.POST,instance=bazar )
            form.save()
            return redirect('currentList')
        except ValueError:
            return render(request, 'bazar/viewlist.html', {'bazar': bazar, 'form': form, 'error': 'Bad data'})

@login_required
def completeBazar(request, bazar_pk):
    bazar = get_object_or_404(Bazar, pk=bazar_pk, user=request.user)
    if request.method == "POST":
        bazar.delete()
        return redirect('currentList')







