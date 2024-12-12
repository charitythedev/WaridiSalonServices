from django.contrib import admin

from application.models import Customer, Salonist, Pricing, Service, ContactRequest

# Register your models here.

admin.site.register(Customer)
admin.site.register(Salonist)
admin.site.register(Pricing)
admin.site.register(Service)
admin.site.register(ContactRequest)
