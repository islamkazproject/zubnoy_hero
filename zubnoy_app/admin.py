from django.contrib import admin
from .models import User, DoctorProfile, RegistrarProfile, ClientProfile, Service, Schedule, Appointment

admin.site.register(User)
admin.site.register(DoctorProfile)
admin.site.register(RegistrarProfile)
admin.site.register(ClientProfile)
admin.site.register(Service)
admin.site.register(Schedule)
admin.site.register(Appointment)
