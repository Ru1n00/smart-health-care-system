from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'smart_health'

urlpatterns = [
    path('', views.index, name='index'),
    path('doctors/', views.DoctorListView.as_view(), name='doctors'),
    path('doctors/<int:pk>/', views.DoctorDetailView.as_view(), name='doctor_detail'),
    path('blood-donors/', views.BloodDonorListView.as_view(), name='blood_donors'),
    path('ambulances/', views.AmbulanceListView.as_view(), name='ambulances'),
    # path('seed/', views.seed, name='seed'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
