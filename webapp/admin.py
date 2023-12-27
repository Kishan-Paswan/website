from django.contrib import admin

# Register your models here.
from .models import gallary
admin.site.register(gallary)

from .models import sign
admin.site.register(sign)

from .models import jobmodel
admin.site.register(jobmodel)

from .models import contactmodel
admin.site.register(contactmodel)

from .models import servicesmodel
admin.site.register(servicesmodel)

from .models import userservices
admin.site.register(userservices)