from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Snaraga
from apps.home.views import form

class ProkatView(View):
    def get(self, request):
        all = list(Snaraga.objects.all())
        spal = list(Snaraga.objects.filter(type="s"))
        snar = list(Snaraga.objects.filter(type="sn"))
        pro = list(Snaraga.objects.filter(type="p"))

        context = {"all":all,
                   "spal":spal,
                   "snar": snar,
                   "pro":pro}
        return render(request, 'services/prokat.html', context)
    def post(self, request):
        return form(request)

class SnaragaDetals(View):
    def get(self, request, id):
        value = get_object_or_404(Snaraga, id=id)
        context = {"value": value}
        return render(request, "services/details_snar.html", context)
    def post(self, request):
        return form(request)

class HostelView(View):
    def get(self, request):
        return render(request, "services/Hostel.html")
    def post(self, request):
        return form(request)


class SertificateView(View):
    def get(self, request):
        return render(request, "services/sertificate.html")
    def post(self, request):
        return form(request)

class PodborView(View):
    def get(self, request):
        return render(request, "services/podbor.html")
    def post(self, request):
        return form(request)

class TransferView(View):
    def get(self, request):
        return render(request, "services/transfer.html")
    def post(self, request):
        return form(request)



# Create your views here.
