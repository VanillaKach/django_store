from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from .forms import UserRegisterForm, UserLoginForm, UserProfileForm
from .models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)

        # Отправка приветственного письма
        send_mail(
            'Добро пожаловать в наш магазин!',
            'Спасибо за регистрацию.',
            'noreply@yourdomain.com',
            [user.email],
            fail_silently=False,
        )
        return response


class UserLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user
