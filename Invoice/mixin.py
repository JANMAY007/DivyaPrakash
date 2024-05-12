from django.contrib import admin
from import_export.admin import ExportActionMixin
from media.AU.au_invoice import make_au_invoice
from .models import CholaMandalam, Poonawalla, AU, Wonder, Aadhar, Axis, Profectus, RBL, HFFC, AYE, \
    Mahindra, YesBankAgri, YesBankSagment, YesBankAHFL, IndiaBulls, NewIndia


class CholaMandalamAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display_fields = [field.name for field in CholaMandalam._meta.get_fields()]
    list_display_fields.remove('price')
    list_display = list_display_fields
    list_filter = ('date', 'customer_name', 'type')
    search_fields = [field.name for field in CholaMandalam._meta.get_fields()]
    list_per_page = 25

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.save()

    def get_exclude(self, request, obj=None):
        if not request.user.is_superuser:
            return ['price']
        return []


class PoonaWallaAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display_fields = [field.name for field in Poonawalla._meta.get_fields()]
    list_display_fields.remove('price')
    list_display = list_display_fields
    list_filter = ('date', 'name_of_borrower', 'type')
    search_fields = [field.name for field in Poonawalla._meta.get_fields()]
    list_per_page = 25

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.save()

    def get_exclude(self, request, obj=None):
        if not request.user.is_superuser:
            return ['price']
        return []


class AUAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display_fields = [field.name for field in AU._meta.get_fields()]
    list_display_fields.remove('price')
    list_display = list_display_fields
    list_filter = ('date', 'rlos_number', 'lead_number', 'lan_number', 'type', 'customer_name', 'reject_hold')
    search_fields = [field.name for field in AU._meta.get_fields()]
    list_per_page = 25

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.save()

    def get_exclude(self, request, obj=None):
        if not request.user.is_superuser:
            return ['price']
        return []

    @admin.action(description='Export Invoice')
    def make_export(self, request, queryset):
        ids = []
        for i in queryset:
            ids.append(i.id)
        queryset = AU.objects.filter(id__in=ids)
        queryset = list(queryset.values())
        return make_au_invoice(queryset)

    actions = [make_export]


class WonderAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display_fields = [field.name for field in Wonder._meta.get_fields()]
    list_display_fields.remove('price')
    list_display = list_display_fields
    list_filter = ('date', 'deal_number', 'type', 'customer_name')
    search_fields = [field.name for field in Wonder._meta.get_fields()]
    list_per_page = 25

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.save()

    def get_exclude(self, request, obj=None):
        if not request.user.is_superuser:
            return ['price']
        return []


class AadharAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display_fields = [field.name for field in Aadhar._meta.get_fields()]
    list_display_fields.remove('price')
    list_display = list_display_fields
    list_filter = ('date', 'customer_name', 'type', 'application_number')
    search_fields = [field.name for field in Aadhar._meta.get_fields()]
    list_per_page = 25

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.save()

    def get_exclude(self, request, obj=None):
        if not request.user.is_superuser:
            return ['price']
        return []


class AxisAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display_fields = [field.name for field in Axis._meta.get_fields()]
    list_display_fields.remove('price')
    list_display = list_display_fields
    list_filter = ('date', 'customer_name', 'type')
    search_fields = [field.name for field in Axis._meta.get_fields()]
    list_per_page = 25

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.save()

    def get_exclude(self, request, obj=None):
        if not request.user.is_superuser:
            return ['price']
        return []


class ProfectusAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display_fields = [field.name for field in Profectus._meta.get_fields()]
    list_display_fields.remove('price')
    list_display = list_display_fields
    list_filter = ('date', 'name_of_applicant', 'type')
    search_fields = [field.name for field in Profectus._meta.get_fields()]
    list_per_page = 25

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.save()

    def get_exclude(self, request, obj=None):
        if not request.user.is_superuser:
            return ['price']
        return []


class RBLAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display_fields = [field.name for field in RBL._meta.get_fields()]
    list_display_fields.remove('price')
    list_display = list_display_fields
    list_filter = ('date', 'customer_name', 'type', 'aps_number', 'survey_number')
    search_fields = [field.name for field in RBL._meta.get_fields()]
    list_per_page = 25

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.save()

    def get_exclude(self, request, obj=None):
        if not request.user.is_superuser:
            return ['price']
        return []


class HFFCAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display_fields = [field.name for field in HFFC._meta.get_fields()]
    list_display_fields.remove('price')
    list_display = list_display_fields
    list_filter = ('date', 'name_of_applicant', 'type')
    search_fields = [field.name for field in HFFC._meta.get_fields()]
    list_per_page = 25

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.save()

    def get_exclude(self, request, obj=None):
        if not request.user.is_superuser:
            return ['price']
        return []


class AYEAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display_fields = [field.name for field in AYE._meta.get_fields()]
    list_display_fields.remove('price')
    list_display = list_display_fields
    list_filter = ('date', 'name_of_applicant', 'type', 'aps')
    search_fields = [field.name for field in AYE._meta.get_fields()]
    list_per_page = 25

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.save()

    def get_exclude(self, request, obj=None):
        if not request.user.is_superuser:
            return ['price']
        return []


class MahindraAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display_fields = [field.name for field in Mahindra._meta.get_fields()]
    list_display_fields.remove('price')
    list_display = list_display_fields
    list_filter = ('date', 'customer_name', 'type', 'aps_number', 'repost_submitted_date')
    search_fields = [field.name for field in Mahindra._meta.get_fields()]
    list_per_page = 25

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.save()

    def get_exclude(self, request, obj=None):
        if not request.user.is_superuser:
            return ['price']
        return []


class YesBankAgriAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display_fields = [field.name for field in YesBankAgri._meta.get_fields()]
    list_display_fields.remove('price')
    list_display = list_display_fields
    list_filter = ('date', 'product_type', 'r_m_fpr_name')
    search_fields = [field.name for field in YesBankAgri._meta.get_fields()]
    list_per_page = 25

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.save()

    def get_exclude(self, request, obj=None):
        if not request.user.is_superuser:
            return ['price']
        return []


class YesBankSagmentAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display_fields = [field.name for field in YesBankSagment._meta.get_fields()]
    list_display_fields.remove('price')
    list_display = list_display_fields
    list_filter = ('date', 'product_type', 'type_of_service', 'client_name')
    search_fields = [field.name for field in YesBankSagment._meta.get_fields()]
    list_per_page = 25

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.save()

    def get_exclude(self, request, obj=None):
        if not request.user.is_superuser:
            return ['price']
        return []


class YesBankAHFLAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display_fields = [field.name for field in YesBankAHFL._meta.get_fields()]
    list_display_fields.remove('price')
    list_display = list_display_fields
    list_filter = ('date', 'type', 'client_name', 'type_of_service')
    search_fields = [field.name for field in YesBankAHFL._meta.get_fields()]
    list_per_page = 25

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.save()

    def get_exclude(self, request, obj=None):
        if not request.user.is_superuser:
            return ['price']
        return []


class IndiaBullsAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display_fields = [field.name for field in IndiaBulls._meta.get_fields()]
    list_display_fields.remove('verification_rate')
    list_display = list_display_fields
    list_filter = ('date', 'verification_type', 'customer_name', 'co_name', 'aps_id')
    search_fields = [field.name for field in IndiaBulls._meta.get_fields()]
    list_per_page = 25

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.save()

    def get_exclude(self, request, obj=None):
        if not request.user.is_superuser:
            return ['price']
        return []


class NewIndiaAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display_fields = [field.name for field in NewIndia._meta.get_fields()]
    list_display_fields = [ele for ele in list_display_fields if ele not in ['court_stamp_fee', 'advocate_fee', 'clerk_fee', 'expenses', 'travelling_expenses', 'other_expenses']]
    list_display = list_display_fields
    list_filter = ('date', 'name_of_party', 'case_number')
    search_fields = [field.name for field in NewIndia._meta.get_fields()]
    list_per_page = 25

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.save()

    def get_exclude(self, request, obj=None):
        if not request.user.is_superuser:
            return ['price']
        return []
