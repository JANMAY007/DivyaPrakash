from django.shortcuts import render
from .models import *
import pandas as pd


from django.contrib.auth.models import User

def home(request):
    table_columns = ['date', 'company_name', 'aps_id', 'customer_name', 'property_address', 'remarks', 'type', 'search_number', 'created_by_id']
    data = pd.DataFrame(columns=table_columns)

    models = [AU, CholaMandalam, Poonawalla, Wonder, Aadhar, Axis, Profectus, RBL, HFFC, AYE, Mahindra, YesBankAgri, YesBankSagment, YesBankAHFL, IndiaBulls, NewIndia, AgriBank]

    row_counter = 0
    for model in models:
        model_data = model.objects.all().values()
        for temp_row in model_data:
            for key, value in temp_row.items():
                if key in table_columns:
                    if key == 'created_by_id':
                        data.loc[row_counter, key] = User.objects.get(id=value).username
                    else:
                        data.loc[row_counter, key] = value
            row_counter += 1

    data = data.fillna('')

    array_2d = data.values
    params = {
        'column_names': table_columns,
        'data': array_2d
    }
    return render(request, 'home.html', params)


