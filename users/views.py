from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from users.models import CustomUser


class UserRegistrationView(TemplateView):
    template_name = 'register.html'


class UserMakeRegistrationView(View):
    """Вью, чтобы зарегистрировать пользователя"""

    def post(self, request, *args, **kwargs):
        data = request.POST

        password1 = data['password1']
        password2 = data['password2']

        if password1 == password2:
            blabla = data['first_name']
            last_name = data['last_name']
            email = data['email_address']
            user = CustomUser.objects.create_user(
                email=email, password=password1,
                first_name=blabla, last_name=last_name,
            )
            return render(request, 'product-list.html')
        else:
            pass