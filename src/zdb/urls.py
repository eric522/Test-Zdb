from django.urls import path
from .views import ZdbListView, ZdbSearchListView

urlpatterns = [
    path('', ZdbListView.as_view(),name='zdb-zdb'),
    path('search/', ZdbSearchListView.as_view(), name='zdb-zdbsearch'),
]