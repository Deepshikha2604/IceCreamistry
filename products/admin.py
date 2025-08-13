from django.contrib import admin
from .models import chef
from .models import iceCream
from .models import Services
from .models import contact

admin.site.register (chef)
admin.site.register (iceCream)
admin.site.register (Services)
admin.site.register(contact)

# Register your models here.
