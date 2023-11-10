from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'dob', 'age', 'gender', 'phone_number', 'email', 'address', 'district', 'branch', 'account_type','materials_provided']