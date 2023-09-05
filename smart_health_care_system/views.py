from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView
from django.db.models import Q

from .models import Doctor, BloodDonor, Ambulance
# Create your views here.
def index(request):
    return render(request, 'smart_health_care_system/index.html', {'current_page': 'home'})


class DoctorListView(ListView):
    model = Doctor
    template_name = 'smart_health_care_system/doctors.html'
    context_object_name = 'doctors'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        if 'query' in request.GET:
            self.query = request.GET['query'].strip()
        else:
            self.query = ''
        
        if self.query:
            self.object_list = self.model.objects.filter(Q(name__icontains=self.query) | Q(speciality__icontains=self.query) | Q(location__icontains=self.query))
            
        else:
            self.object_list = self.model.objects.all()
        
        context = self.get_context_data()
        context['current_page'] = 'doctors'
        return self.render_to_response(context)


class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'smart_health_care_system/doctor_detail.html'
    context_object_name = 'doctor'


class BloodDonorListView(ListView):
    model = BloodDonor
    template_name = 'smart_health_care_system/blood_donors.html'
    context_object_name = 'blood_donors'
    paginate_by = 20


    def get(self, request, *args, **kwargs):
        if 'query' in request.GET:
            self.query = request.GET['query'].strip()
        else:
            self.query = ''
        
        if self.query:
            self.object_list = self.model.objects.filter(Q(name__icontains=self.query) | Q(blood_group__icontains=self.query) | Q(location__icontains=self.query))
            
        else:
            self.object_list = self.model.objects.all()
        
        context = self.get_context_data()
        context['current_page'] = 'donors'
        return self.render_to_response(context)


class AmbulanceListView(ListView):
    model = Ambulance
    template_name = 'smart_health_care_system/ambulances.html'
    context_object_name = 'ambulances'
    paginate_by = 20

    def get(self, request, *args, **kwargs):
        if 'query' in request.GET:
            self.query = request.GET['query'].strip()
        else:
            self.query = ''
        
        if self.query:
            self.object_list = self.model.objects.filter(Q(name__icontains=self.query) | Q(district__icontains=self.query))
            
        else:
            self.object_list = self.model.objects.all()
        
        context = self.get_context_data()
        context['current_page'] = 'ambulances'
        return self.render_to_response(context)



# seeding the database
def seed(request):
    from .seeds import doctors

    if Doctor.objects.count() < 30:
        for doctor in doctors:
            Doctor.objects.create(
                name=doctor[0],
                speciality=doctor[1],
                degrees_earned=doctor[2],
                position=doctor[3],
                location=doctor[4],
                visiting_place=doctor[5],
                visiting_hours=doctor[6],
                contact_info=doctor[7],
                img=doctor[8],
            )
    
    if BloodDonor.objects.count() < 30:
        from .seeds import blood_donors

        for blood_donor in blood_donors:
            BloodDonor.objects.create(
                name=blood_donor[0],
                blood_group=blood_donor[1],
                location=blood_donor[2],
                contact_info=blood_donor[3],
            )
    
    if Ambulance.objects.count() < 30:
        from .seeds import ambulances

        for ambulance in ambulances:
            Ambulance.objects.create(
                name=ambulance[0],
                contact_info=ambulance[1],
                district=ambulance[2],
            )

    return HttpResponse("Seeded successfully")