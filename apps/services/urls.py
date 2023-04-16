from django.urls import path
from .views import ProkatView, SnaragaDetals, HostelView, SertificateView, PodborView, TransferView

app_name = 'services'
urlpatterns = [
    path('procat', ProkatView.as_view(), name='prokat'),
    path('shiksha',HostelView.as_view(), name = 'hostel'),
    path('prokat/<int:id>', SnaragaDetals.as_view(), name = 'snaraga'),
    path('sertificate',SertificateView.as_view(), name = 'sertificate'),
    path('podbor', PodborView.as_view(), name = 'podbor'),
    path('transfer', TransferView.as_view(), name= 'transfer'),
    ]