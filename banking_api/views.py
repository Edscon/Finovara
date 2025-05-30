from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
import json
from keys.models import ApiToken
from .views_requests_api import *
from core.views import get_menu_items
from .models import Institutions

import time


def get_institutions():
    try:
        institutions = list(Institutions.objects.all())
        
        #Ordenamos para que los principales bancos de España salgan primero
        order_names =['Banco Santander', 'BBVA', 'CaixaBank', 'Banco de Sabadell', 'Bankinter', 
                      'ING', 'Openbank', 'Unicaja Banco', 'Abanca', 'Kutxabank', 'Grupo Cajamar', 
                      'IberCaja' 'LiberBank', 'Stripe']
        order_index = {name: i for i, name in enumerate(order_names)}
        institutions.sort(key=lambda i: order_index.get(i.name, len(order_names)))

        return institutions
    except Exception as e:
        print(f'Error fetching institutions: {e}')
        return []

def app(request):

    institutions = get_institutions()

    context = {
        'menu_name': 'app',
        'institutions': institutions,
        
    }

    return render(request, 'app_dashboard.html', context)


async def agreement_institution(request, id_code):
    access_key = await get_valid_access_token()
    print(access_key)
    try:
        institution = await sync_to_async(Institutions.objects.get)(id=id_code)
        institution_id = institution.id
    except Institutions.DoesNotExist:
        return HttpResponseServerError("Institution not found")

    #Only for sandbox!!!!!!
    institution_id = 'SANDBOXFINANCE_SFIN0000'

    # Create agreement
    agreement = await async_create_agreement(
        token=access_key,
        institution_id=institution_id,
        max_days=90,
        valid_days=90,
        access_scope=["balances", "details", "transactions"]
    )
    
    # Create requisition
    redirect_url = request.build_absolute_uri(reverse('app'))
    requisition = await create_requisition(
        token=access_key,
        redirect_url=redirect_url,
        institution_id=institution_id,
        reference='ref123',
        agreement_id=agreement['id'],
        user_language='ES'
    )
    print(f'Agreement created: {requisition}')
    return JsonResponse(requisition)


def dashboard_proba(request):
    requisition_id = request.GET.get('ref')  # obte requisition ID de la URL
    requisition_id = '13cd2adc-6c4c-4e40-88de-40c1896528a9' # Sandbox

    #access_key = ApiKey.objects.filter(name='access_key').first()
    
    account_data = {}


    context = {
        'account_data': account_data,
    }

    return render(request, 'dashboard_proba.html', context)
