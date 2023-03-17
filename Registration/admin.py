from django.contrib import admin
from .models import log_in_registtration_student
from .models import log_in_registtration_teacher



# Register your models here.
admin.site.register(log_in_registtration_student)
admin.site.register(log_in_registtration_teacher)
