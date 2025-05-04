from django.shortcuts import render
from django.urls import reverse
import json
from keys.models import ApiKey
from .views_requests_api import *

def connection(request):

    #access_key = ApiKey.objects.filter(name='access_key').first()
    access_key = get_access_token()['access']
    print(access_key)
    institutions = get_institutions(access_key, 'es')

    #Para Pruebas
    sandbox_institution_id = 'SANDBOXFINANCE_SFIN0000'

    # Crear un acuerdo para una institución
    agreement_data = create_agreement(
        token=access_key,
        institution_id= sandbox_institution_id
    )

    agreement_id = agreement_data.get('id')

    # Crear una requisición de autenticación bancaria
    requisition_data = create_requisition(
        token=access_key,
        agreement_id=agreement_id,
        institution_id=sandbox_institution_id,
        redirect_url= request.build_absolute_uri(reverse('dashboard')),
        reference=agreement_id,  # Podrías usar un UUID si quieres algo único
        user_language='ES'
    )


    context = {
        'institutions': institutions,
        'url_link': requisition_data.get('link'),
    }

    # You can add any logic here if needed
    return render(request, 'connection.html', context)

def dashboard_proba(request):
    requisition_id = request.GET.get('ref')  # obte requisition ID de la URL
    requisition_id = '13cd2adc-6c4c-4e40-88de-40c1896528a9' # Sandbox

    access_key = ApiKey.objects.filter(name='access_key').first()
    
    account_data = {}

    if requisition_id and access_key:
        try:
            requisition = get_requisition_details(access_key, requisition_id)
            print(requisition)
            accounts = requisition.get('accounts', [])
            
            for account_id in accounts:
                balance = get_account_balance(access_key, account_id)
                #transactions = get_account_transactions(access_key, account_id)

                account_data[account_id] = {
                    'balance': balance,
                    #'transactions': transactions
                }

        except Exception as e:
            print(f"Error carregant dades de compte: {e}")

    context = {
        'account_data': account_data,
    }

    return render(request, 'dashboard_proba.html', context)
