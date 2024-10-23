from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .models import Admin, UserCourse, Course
from django.contrib.auth.decorators import login_required
from .forms import CustomLoginForm
from django.contrib.auth.models import User

def userhome(request):
    if not request.user.is_authenticated:
        return render(request, 'userhome.html', {})

    usercourses = UserCourse.objects.filter(user=request.user).select_related('course')
    courses = Course.objects.all()

    data = {
        'usercourses': usercourses,
        'courses': courses
    }
    return render(request, 'userhome.html', data)

@login_required
def adminhome(request):
    courses = Course.objects.all()
    users = User.objects.all()
    usercourses = UserCourse.objects.all()
    data = {'courses': courses, 'users': users, 'usercourses': usercourses}
    return render(request, 'adminhome.html', data)

def login(request):
    userform = CustomLoginForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            admins = Admin.objects.all()
            if user in admins:
                return redirect('adminhome')
            return redirect('userhome')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html', {'form': userform})
