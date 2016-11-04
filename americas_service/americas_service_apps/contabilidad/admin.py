from django.contrib import admin
from .models.Debe import Debe
from .models.Haber import Haber

# Register your models here.
admin.site.register(Debe)
admin.site.register(Haber)
