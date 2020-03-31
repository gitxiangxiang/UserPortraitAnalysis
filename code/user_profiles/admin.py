from django.contrib import admin

# Register your models here.
from user_profiles.models.PersonalAppeal import PersonalAppeal
from .models import PersonalAppeal_mongo

admin.site.register(PersonalAppeal)
# admin.site.register(PersonalAppeal_mongo.PersonalAppeal)
