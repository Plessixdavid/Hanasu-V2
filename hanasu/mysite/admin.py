from django.contrib import admin
from .models import Ideotype, Ideogramm, Documentary, Maneki

# Register your models here.
admin.site.register(Ideogramm)
admin.site.register(Ideotype)
admin.site.register(Documentary)
admin.site.register(Maneki)