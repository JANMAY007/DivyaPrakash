from django.contrib import admin
from import_export.admin import ExportActionMixin
from .models import CholaMandalam, Poonawalla, AU, Wonder, Aadhar, Axis, Profectus, RBL, HFFC, AYE,\
    Mahindra, YesBankAgri, YesBankSagment, YesBankAHFL, IndiaBulls, NewIndia


class CholaMandalamAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = [field.name for field in CholaMandalam._meta.get_fields()]
    list_filter = ('date', 'customer_name', 'type')
    search_fields = [field.name for field in CholaMandalam._meta.get_fields()]
    list_per_page = 25


class PoonaWallaAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = [field.name for field in Poonawalla._meta.get_fields()]
    list_filter = ('date', 'pg_number', 'name_of_borrower', 'type')
    search_fields = [field.name for field in Poonawalla._meta.get_fields()]
    list_per_page = 25


class AUAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = [field.name for field in AU._meta.get_fields()]
    list_filter = ('date', 'rlos_number', 'lead_number', 'lan_number', 'type', 'customer_name', 'reject_hold')
    search_fields = [field.name for field in AU._meta.get_fields()]
    list_per_page = 25


class WonderAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = [field.name for field in Wonder._meta.get_fields()]
    list_filter = ('date', 'deal_number', 'type', 'customer_name')
    search_fields = [field.name for field in Wonder._meta.get_fields()]
    list_per_page = 25


class AadharAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = [field.name for field in Aadhar._meta.get_fields()]
    list_filter = ('date', 'customer_name', 'type', 'application_number')
    search_fields = [field.name for field in Aadhar._meta.get_fields()]
    list_per_page = 25


class AxisAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = [field.name for field in Axis._meta.get_fields()]
    list_filter = ('date', 'customer_name', 'type')
    search_fields = [field.name for field in Axis._meta.get_fields()]
    list_per_page = 25


class ProfectusAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = [field.name for field in Profectus._meta.get_fields()]
    list_filter = ('date', 'name_of_applicant', 'type')
    search_fields = [field.name for field in Profectus._meta.get_fields()]
    list_per_page = 25


class RBLAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = [field.name for field in RBL._meta.get_fields()]
    list_filter = ('date', 'customer_name', 'type', 'aps_number', 'survey_number')
    search_fields = [field.name for field in RBL._meta.get_fields()]
    list_per_page = 25


class HFFCAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = [field.name for field in HFFC._meta.get_fields()]
    list_filter = ('date', 'name_of_applicant', 'type')
    search_fields = [field.name for field in HFFC._meta.get_fields()]
    list_per_page = 25


class AYEAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = [field.name for field in AYE._meta.get_fields()]
    list_filter = ('date', 'name_of_applicant', 'type', 'aps')
    search_fields = [field.name for field in AYE._meta.get_fields()]
    list_per_page = 25


class MahindraAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = [field.name for field in Mahindra._meta.get_fields()]
    list_filter = ('date', 'customer_name', 'type', 'aps_number', 'repost_submitted_date')
    search_fields = [field.name for field in Mahindra._meta.get_fields()]
    list_per_page = 25


class YesBankAgriAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = [field.name for field in YesBankAgri._meta.get_fields()]
    list_filter = ('date', 'product_type', 'r_m_fpr_name')
    search_fields = [field.name for field in YesBankAgri._meta.get_fields()]
    list_per_page = 25


class YesBankSagmentAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = [field.name for field in YesBankSagment._meta.get_fields()]
    list_filter = ('date', 'product_type', 'type_of_service', 'client_name')
    search_fields = [field.name for field in YesBankSagment._meta.get_fields()]
    list_per_page = 25


class YesBankAHFLAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = [field.name for field in YesBankAHFL._meta.get_fields()]
    list_filter = ('date', 'type', 'client_name', 'type_of_service')
    search_fields = [field.name for field in YesBankAHFL._meta.get_fields()]
    list_per_page = 25


class IndiaBullsAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = [field.name for field in IndiaBulls._meta.get_fields()]
    list_filter = ('date', 'verification_type', 'customer_name', 'co_name', 'aps_id')
    search_fields = [field.name for field in IndiaBulls._meta.get_fields()]
    list_per_page = 25


class NewIndiaAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = [field.name for field in NewIndia._meta.get_fields()]
    list_filter = ('date', 'name_of_party', 'case_number')
    search_fields = [field.name for field in NewIndia._meta.get_fields()]
    list_per_page = 25
