from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def login(request):
    return render(request,"account/login.html",{})

# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, f'خوش اومدی، {username}!')
#                 return HttpResponseRedirect(reverse('home'))
#             else:
#                 messages.error(request, 'نام کاربری یا رمز عبور اشتباهه!')
#         else:
#             messages.error(request, 'لطفاً اطلاعات معتبر وارد کن!')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'account/login.html', {'form': form})
#
# def logout_view(request):
#     logout(request)
#     messages.success(request, 'با موفقیت 0خارج شدی!')
#     return redirect('login')