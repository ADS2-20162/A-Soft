from django.contrib import admin

# Register your models here.
from .models.Socio import Socio
from .models.Conyuge import Conyuge
from .models.Email import Email

admin.site.register(Socio)
admin.site.register(Conyuge)
admin.site.register(Email)
