from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from .models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from accounts.forms import SignupForm, ProfileForm
from django.contrib.auth.views import LoginView, logout_then_login
from django.contrib.auth import login as auth_login
import time
import requests
from backend import settings

login = LoginView.as_view(template_name="accounts/login_form.html")

# def login(request):
#     if request.method == 'POST':
#         form = LoginForm (request.POST)

def logout(request):
    messages.success(request, '로그아웃되었습니다.')
    return logout_then_login(request)


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            signed_user = form.save()
            auth_login(request, signed_user)
            messages.success(request, "회원가입 성공")
            next_url = request.GET.get('next', '/')
            return redirect(next_url)

    else:
        form = SignupForm()

    return render(request, 'accounts/signup_form.html', {
        'form': form,
    })


@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "프로필을 수정/저장했습니다.")
            return redirect("profile_edit")

    else:
        form = ProfileForm(instance=request.user)

    return render(request, "accounts/profile_edit_form.html", {
        "form": form,
    })


@login_required
def start(request):
    messages.success(request, "녹음을 시작했습니다.")
    redirect_url = request.META.get("HTTP_REFERER", "root")
    user = request.user
    user.check = True
    user.save()
    print(User.objects.all().first().check)
    return redirect(redirect_url)


@login_required
def end(request):
    messages.success(request, "녹음을 끝냅니다.")
    redirect_url = request.META.get("HTTP_REFERER", "root")
    user = request.user
    user.check = False
    user.save()
    print(User.objects.all().first().check)
    return redirect(redirect_url)


def check(request):
    user = User.objects.all().first()
    requirements = dict()
    requirements['check'] = user.check
    return JsonResponse(requirements)

