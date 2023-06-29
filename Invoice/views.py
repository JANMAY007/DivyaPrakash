from django.shortcuts import render
from .models import *
from media.AU import au_invoice
import pandas as pd


from django.contrib.auth.models import User

def home(request):
    model_fields = [field.name for field in AU._meta.get_fields()]
    model_fields += [field.name for field in CholaMandalam._meta.get_fields()]
    model_fields += [field.name for field in Poonawalla._meta.get_fields()]
    model_fields += [field.name for field in Wonder._meta.get_fields()]
    model_fields += [field.name for field in Aadhar._meta.get_fields()]
    model_fields += [field.name for field in Axis._meta.get_fields()]
    model_fields += [field.name for field in Profectus._meta.get_fields()]
    model_fields += [field.name for field in RBL._meta.get_fields()]
    model_fields += [field.name for field in HFFC._meta.get_fields()]
    model_fields += [field.name for field in AYE._meta.get_fields()]
    model_fields += [field.name for field in Mahindra._meta.get_fields()]
    model_fields += [field.name for field in YesBankAgri._meta.get_fields()]
    model_fields += [field.name for field in YesBankSagment._meta.get_fields()]
    model_fields += [field.name for field in YesBankAHFL._meta.get_fields()]
    model_fields += [field.name for field in IndiaBulls._meta.get_fields()]
    model_fields += [field.name for field in NewIndia._meta.get_fields()]
    model_fields += [field.name for field in AgriBank._meta.get_fields()]

    sorted_set = sorted(set(model_fields))
    table_columns = list(sorted_set)

    data = pd.DataFrame(columns=list(table_columns))

    models = [AU, CholaMandalam, Poonawalla, Wonder, Aadhar, Axis, Profectus, RBL, HFFC, AYE, Mahindra, YesBankAgri, YesBankSagment, YesBankAHFL, IndiaBulls, NewIndia, AgriBank]

    row_counter = 0
    for model in models:
        model_data = model.objects.all().values()
        for temp_row in model_data:
            for key, value in temp_row.items():
                data.loc[row_counter, key] = value
            row_counter += 1

    data = data.fillna('')

    array_2d = data.values
    params = {
        'column_names': table_columns,
        'data': array_2d
    }
    return render(request, 'home.html', params)


