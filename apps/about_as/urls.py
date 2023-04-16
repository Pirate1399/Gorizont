from django.urls import path
from .views import AboutView, PeopleView

app_name = 'about_as'
urlpatterns = [
    path('', AboutView.as_view(), name='about'),
    path('single/<int:people_id>', PeopleView.as_view(), name='single'),
    ]