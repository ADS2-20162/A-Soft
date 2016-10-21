from django.contrib import admin
# from django.contrib.contenttypes.models import ContentType

# Register your models here.
from .models.RubroCobranza import RubroCobranza

admin.site.register(RubroCobranza)
