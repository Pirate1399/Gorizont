from django.shortcuts import render, get_object_or_404
from  django.views import View
from .models import People
from apps.home.views import form


class AboutView(View):
    def get(self, request):
        data = list(People.objects.all())
        context = {"people":data}
        return render(request, 'about_as/about.html', context)
    def post(self, request):
        return form(request)

class PeopleView(View):
    def get(self, request, people_id):
        data = get_object_or_404(People, id = people_id)
        data.skill_1 = str(data.skill_1).split(",")
        data.skill_2 = str(data.skill_2).split(",")
        data.skill_3 = str(data.skill_3).split(",")
        data.skill_4 = str(data.skill_4).split(",")
        context = {"people":data}
        return render(request, 'about_as/single.html', context)
    def post(self, request):
        return form(request)

# Create your views here.
