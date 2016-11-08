from django.contrib import admin
from .models.debe import Debe
from .models.haber import Haber

# Register your models here.
admin.site.register(Debe)
admin.site.register(Haber)
