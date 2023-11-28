from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.views.generic import TemplateView, View
from django.shortcuts import redirect
from django.conf import settings
from django.utils.timezone import now
from users.models import User


class GetOrCreateUser(TemplateView):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        print("\n============================\n User Checking!",flush=True)
        if self.request.user.is_authenticated:
            print("\n============================\n User is authenticated!",flush=True)
            return HttpResponseRedirect(reverse('index'))
        return super().get(request, *args, **kwargs)

    def post(self, request):
        email = request.POST.get('email')
        name = request.POST.get('name')

        user = User.objects.filter(email=email)
        if user.exists():
            user = user.first()
        else:
            user = User.objects.create(email=email, name=name)
            user.set_password(settings.DEFAULT_PASSWORD)
            user.save()

        user.last_login = now()
        user.save()

        auth_user = authenticate(request, username=user.email, password=settings.DEFAULT_PASSWORD)

        if auth_user:
            login(request, auth_user)
            return redirect("/")

        return TemplateResponse(request, 'login.html')


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("/login/")
