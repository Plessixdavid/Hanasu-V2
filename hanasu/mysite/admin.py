from django.contrib import admin
from .models import Ideotype, Ideogramm, Documentary, Maneki, Score, Trophy

# Register your models here.
admin.site.register(Ideogramm)
admin.site.register(Ideotype)
admin.site.register(Documentary)
admin.site.register(Maneki)
admin.site.register(Score)
admin.site.register(Trophy)