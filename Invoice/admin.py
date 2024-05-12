from django.contrib import admin
from .models import *
from .mixin import *


admin.site.register(PersonalDetails)
admin.site.register(CholaMandalam, CholaMandalamAdmin)
admin.site.register(Poonawalla, PoonaWallaAdmin)
admin.site.register(AU, AUAdmin)
admin.site.register(Wonder, WonderAdmin)
admin.site.register(Aadhar, AadharAdmin)
admin.site.register(Axis, AxisAdmin)
admin.site.register(Profectus, ProfectusAdmin)
admin.site.register(RBL, RBLAdmin)
admin.site.register(HFFC, HFFCAdmin)
admin.site.register(AYE, AYEAdmin)
admin.site.register(Mahindra, MahindraAdmin)
admin.site.register(YesBankAgri, YesBankAgriAdmin)
admin.site.register(YesBankSagment, YesBankSagmentAdmin)
admin.site.register(YesBankAHFL, YesBankAHFLAdmin)
admin.site.register(IndiaBulls, IndiaBullsAdmin)
admin.site.register(NewIndia, NewIndiaAdmin)
admin.site.register(AgriBank)
