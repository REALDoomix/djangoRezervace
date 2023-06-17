from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('zakaznici', views.zakaznici, name='zakaznici'),
    path('zakaznik/<int:pk>', views.ZakaznikDetailView.as_view(), name='zakaznik_detail'),
]