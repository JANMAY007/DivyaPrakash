from django.shortcuts import render
from .models import AU
from media.AU import au_invoice

def home(request):
    queryset = AU.objects.all()
    # print(queryset.values())
    # au_invoice.make_au_invoice(queryset=queryset.values())
    return render(request, 'home.html', {'queryset': queryset})
