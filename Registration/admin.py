from django.contrib import admin
from .models import Notic, log_in_registtration_student
from .models import log_in_registtration_teacher
from .models import thumnail
from .models import Playlist
from .models import Quize_thumnail
from .models import Quize_questions

# Register your models here.
admin.site.register(log_in_registtration_student)
admin.site.register(log_in_registtration_teacher)
admin.site.register(thumnail)
admin.site.register(Playlist)
admin.site.register(Quize_thumnail)
admin.site.register(Quize_questions)
admin.site.register(Notic)