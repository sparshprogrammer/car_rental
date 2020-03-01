from django.contrib import admin

# Register your models here.
from cars.models import Cars

class CarsAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']


admin.site.register(Cars, None)