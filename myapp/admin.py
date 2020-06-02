from django.contrib import admin
from myapp.models import person
from myapp.models import doctors
from myapp.models import hospital
from myapp.models import NGO
from myapp.models import appointment
from myapp.models import patient
from myapp.models import prediction
from myapp.models import report
from myapp.models import donation
from myapp.models import user
from myapp.models import Review
from myapp.models import Reg
from myapp.models import Login
from myapp.models import Changepassword
from myapp.models import HandS
from myapp.models import Contact
# Register your models here.
admin.site.register(person)
admin.site.register(doctors)
admin.site.register(hospital)
admin.site.register(NGO)
admin.site.register(appointment)
admin.site.register(patient)
admin.site.register(prediction)
admin.site.register(report)
admin.site.register(donation)
admin.site.register(user)
admin.site.register(Review)
admin.site.register(Reg)
admin.site.register(Login)
admin.site.register(Changepassword)
admin.site.register(HandS)
admin.site.register(Contact)