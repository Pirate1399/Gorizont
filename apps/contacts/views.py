from django.shortcuts import render, redirect
from django.views import View
from apps.contacts.forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail


# Create your views here.
class ContactsView(View):
    def get(self, request):
        return render(request, 'contacts/contacts.html')
    def post(self, request):
        form = ContactForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            subject = f'{name} написал сообщение на сайте'
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            send_mail(subject, f'Имя: {name}\ne-mail:{email}\nСообщение:{message}', 'evgeny.samovol@yandex.ru',
                      ['samovole@gmail.com'])
            messages.success(request, 'Сообщение отправлено')
        return redirect('home:index')