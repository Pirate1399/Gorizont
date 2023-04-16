from django.shortcuts import render, get_object_or_404, _get_queryset, redirect
from django.views import View
from django.core.paginator import Paginator
from django.core.mail import send_mail
from datetime import datetime
from django.contrib import messages

from apps.tours.models import Tour, Calendar
from apps.shop.models import Product
from apps.home.forms import ConactForm
# Create your views here.
class HomeView(View):
    def get(self, request):
        tours = list(Tour.objects.all())
        tours = sorted(tours, key=lambda tour: tour.priority)
        next_tour = search_next_tour()
        paginator = Paginator(tours, 4)
        p1 = paginator.page(1).object_list
        short_list = []
        for i in p1:
            a = i.description[0:150]
            short_list.append(a)
        data = {"p1": (p1[0], short_list[0]),
                "p2": (p1[1], short_list[1]),
                "p3": (p1[2], short_list[2]),
                "p4": (p1[3], short_list[3]),
                "next_tour": next_tour,
                "shop_pictures": products()}
        return render(request, 'home/index.html', data)
    def post(self, request):
        return form(request)


def form(request):
    form = ConactForm(data=request.POST)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        subject = f'{name} просит перезвонить!'
        telephone = form.cleaned_data.get('telephone')
        send_mail(subject, f'Имя: {name}\nТелефон:{telephone}', 'evgeny.samovol@yandex.ru',
                          ['samovole@gmail.com'])
        messages.success(request, 'Сообщение отправлено')
    return redirect('home:index')


def search_next_tour():
    date = list(Calendar.objects.all())
    tours = list(Tour.objects.all())
    date_list = [i for i in date if i.start_date > datetime.today().date()]
    d = tours[0]
    for j in date_list:
        if j.start_date == min([i.start_date for i in date_list]):
            d = j

    tour = tours[0]
    for i in tours:
        if str(d.name).split(",")[0] == i.name:
            tour = i
    return tour


def products():
    data = list(Product.objects.all())
    pictures = [i.title_foto for i in data]
    return pictures

