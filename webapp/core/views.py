from django.contrib.auth import authenticate, login, models, logout
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from users.models import Gallery


def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('dashboard'))
    else:
        return HttpResponseRedirect(reverse('login_user'))

@login_required(login_url='login_user')
def dashboard(request):
    gallery_list = [gallery.to_json for gallery in Gallery.objects.all()]
    return render(request,
                  'dashboard.html',
                  {
                      'gallery_list': gallery_list
                  },
                  )


def login_user(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            return render(request, 'login.html', {'message': 'Invalid Username or Password'})
    else:
        return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_user'))
