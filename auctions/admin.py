from django.contrib import admin
from .models import User, listings, Category

# Register your models here.
admin.site.register(User)
admin.site.register(listings)
admin.site.register(Category)
