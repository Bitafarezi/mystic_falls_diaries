from django.shortcuts import render, redirect
from django.views import View
from .forms import SupernaturalSignupForm
# Create your views here.


class SignupView(View):
    template_name = 'supernatural_users/signup.html'

    def get(self, request):
        form = SupernaturalSignupForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SupernaturalSignupForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the login page immediately after a successful signup
            return redirect('login') 
        return render(request, self.template_name, {'form': form})