from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Menu)
admin.site.register(Orders)
admin.site.register(Toppings)
admin.site.register(Cart)