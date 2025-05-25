from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
import json
from keys.models import ApiToken
from .views_requests_api import *
from core.views import get_menu_items

import time

@csrf_exempt
async def institutions_api(request):
    try:
        access_key = await get_valid_access_token()
        institutions = await async_get_institutions(access_key, 'es')

        #Ordenamos para que los principales bancos de España salgan primero
        order_names =['Banco Santander', 'BBVA', 'CaixaBank', 'Banco de Sabadell', 'Bankinter', 
                      'ING', 'Openbank', 'Unicaja Banco', 'Abanca', 'Kutxabank', 'Grupo Cajamar', 
                      'IberCaja' 'LiberBank', 'Stripe']
        order_index = {n:i for i,n in enumerate(order_names)}
        institutions = sorted(institutions, key=lambda i: order_index.get(i['name'], len(order_names)))

        return JsonResponse(institutions, safe=False)
    except requests.RequestException as e:
        return HttpResponseServerError(f"Error obtenint institucions: {str(e)}")


def app(request):

    institutions = {}
    requisition_data = {}

    context = {
        'menu_name': 'app',
        'institutions': institutions,
        'url_link': requisition_data.get('link'),
        
    }

    return render(request, 'app_dashboard.html', context)

def dashboard_proba(request):
    requisition_id = request.GET.get('ref')  # obte requisition ID de la URL
    requisition_id = '13cd2adc-6c4c-4e40-88de-40c1896528a9' # Sandbox

    #access_key = ApiKey.objects.filter(name='access_key').first()
    
    account_data = {}


    context = {
        'account_data': account_data,
    }

    return render(request, 'dashboard_proba.html', context)
