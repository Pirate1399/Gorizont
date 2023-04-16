from django.urls import path
from .views import ToursView, ShowTour, ToursViewSortLevel, ProGorView, CalendarView, ExcursionsView, ShowExursion,\
    ToursViewSortType, ToursViewSortLoc

app_name = 'tours'
urlpatterns = [
    path('', ToursView.as_view(), name='tours'),
    path('calendar', CalendarView.as_view(), name='calendar'),
    path('progoriki', ProGorView.as_view(), name='progor'),
    path('excursions', ExcursionsView.as_view(), name='excursions'),
    path('level/<level>', ToursViewSortLevel.as_view(), name='tour_sort_level'),
    path('type/<type>', ToursViewSortType.as_view(), name='tour_sort_type'),
    path('location/<location>', ToursViewSortLoc.as_view(), name='tour_sort_location'),
    path('<tour_name>', ShowTour.as_view(), name='show_tour'),
    path('excursions/<exursion_name>', ShowExursion.as_view(), name='show_exursion'),

    ]