from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView
from django.core.paginator import Paginator


from datetime import datetime, timezone, timedelta
from .models import Tour, Calendar, Excursion

from apps.home.views import form
# Create your views here.


def paginator(request, data):
    """
    Functiom for pagination tours.
    Not use for Exursions and Sort Level!!!
    :param request: request from View
    :param data: list from View
    :return: context
    """
    paginator = Paginator(data, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"tours": page_obj,
               "paginator": paginator}
    return context

class ToursView(ListView):
    def get(self, request):
        data = list(Tour.objects.all())
        data =sorted(data, key=lambda tour: tour.priority)
        context = paginator(request,data)
        print(context)
        return render(request, 'tours/tours.html', context)
    def post(self, request):
        return form(request)


class ShowTour(View):
    def get(self, request, tour_name):
        data = get_object_or_404(Tour, name=tour_name)
        data.text = data.text.split("\n")
        print(data.type)
        context = {"tour": data}
        return render(request, 'tours/show_tour.html', context)
    def post(self, request):
        return form(request)

class ToursViewSortLevel(View):
    def get(self, request, level):
        sort_data = []
        data = list(Tour.objects.all())
        data = sorted(data, key=lambda tour: tour.priority)
        for i in data:
            if str(i.level) == level:
                sort_data.append(i)
        context = paginator(request, sort_data)
        return render(request, 'tours/tour_sort_level.html', context)
    def post(self, request):
        return form(request)


class ProGorView(View):
    def get(self, request):
        data = list(Tour.objects.filter(pro_gor = True))
        context = {"tours":data}
        return render(request, 'tours/pro_goriki.html', context)
    def post(self, request):
        return form(request)

class CalendarView(View):
    def get(self, request):
        tours = list(Tour.objects.all())
        calendar = list(Calendar.objects.all())
        data = []
        for i in calendar:
            tour = None
            for j in tours:
                if str(i.name).split(",")[0] == j.name:
                    tour = j
            data.append([i, tour])
        print(len(data))
        context = {f"{i}month":[] for i in range(1,13)}
        p = []
        for i in range(1,13):
            p.clear()
            for j in data:
                if i == j[0].start_date.month:
                    context[f"{i}month"].append(j)

        tz = timezone(timedelta(hours=8)) #Это я возвращаю Иркутское время и дату и добавляю в словарь
        dt = datetime.now(tz=tz)
        context["today"] = dt.strftime("%d.%m.%Y %H:%M")
        context["year"] = dt.year
        return render(request, 'tours/calendar.html', context)
    def post(self, request):
        return form(request)

class ExcursionsView(View):
    def get(self, request):
        data = list(Excursion.objects.all())
        data = sorted(data, key=lambda excursion: excursion.priority)
        paginator = Paginator(data, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {"excurtions": page_obj,
                   "paginator": paginator}
        print(context)
        return render(request, 'tours/excursions.html', context)
    def post(self, request):
        return form(request)

class ShowExursion(View):
    def get(self, request, exursion_name):
        data = get_object_or_404(Excursion, name=exursion_name)
        data.description = data.description.split("\n")
        context = {"tour": data}
        return render(request, 'tours/show_exursion.html', context)
    def post(self, request):
        return form(request)


class ToursViewSortType(View):
    def get(self, request, type):
        sort_data = []
        data = list(Tour.objects.all())
        data = sorted(data, key=lambda tour: tour.priority)
        for i in data:
            if str(i.type) == type:
                sort_data.append(i)
        context = paginator(request, sort_data)
        return render(request, 'tours/tour_sort_level.html', context)
    def post(self, request):
        return form(request)

class ToursViewSortLoc(View):
    def get(self, request, location):
        sort_data = []
        data = list(Tour.objects.all())
        data = sorted(data, key=lambda tour: tour.priority)
        for i in data:
            print(i.location)
            if str(i.location) == location:
                sort_data.append(i)
        context = paginator(request, sort_data)
        return render(request, 'tours/tour_sort_level.html', context)
    def post(self, request):
        return form(request)