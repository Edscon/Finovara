import os
from asgiref.sync import sync_to_async
from dotenv import load_dotenv
from datetime import datetime, timedelta
from django.utils import timezone
import requests
import httpx
from keys.models import ApiToken 

load_dotenv()

def get_env_secrets():
    return {
        "secret_id": os.getenv("GOCARDLESS_SECRETID"),
        "secret_key": os.getenv("GOCARDLESS_SECRETKEY")
    }

def json_headers(token=None):
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers

# Constants
BASE_API_URL = "https://bankaccountdata.gocardless.com/api/v2"
ACCESS_KEY_URL = f"{BASE_API_URL}/token/new/"
TOKEN_REFRESH_URL = f"{BASE_API_URL}/token/refresh/"
INSTITUTIONS_URL = f"{BASE_API_URL}/institutions/"
AGREEMENTS_URL = f"{BASE_API_URL}/agreements/enduser/"
REQUISITIONS_URL = f"{BASE_API_URL}/requisitions/"
ACCOUNTS_URL = f"{BASE_API_URL}/accounts/"

# 1. Get Access Token
@sync_to_async
def get_token_from_db():
    return ApiToken.objects.first()

@sync_to_async
def save_token(data):

    token = ApiToken.objects.update_or_create(
        id=1,
        defaults={
            'access_token': data['access'],
            'refresh_token': data['refresh'],
            'access_expires_at': timezone.now() + timedelta(seconds=data['access_expires']),
            'refresh_expires_at': timezone.now() + timedelta(seconds=data['refresh_expires']),
        }
    )[0]

    return token.access_token

async def generate_new_tokens():
    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.post(
            ACCESS_KEY_URL,
            headers=json_headers(),
            json=get_env_secrets()
        )
        response.raise_for_status()
        data = response.json()

    return await save_token(data)

async def refresh_tokens(refresh_token):
    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.post(
            TOKEN_REFRESH_URL,
            headers=json_headers(),
            json={"refresh": refresh_token}
        )
        response.raise_for_status()
        data = response.json()

    return await save_token(data)

async def get_valid_access_token():
    token = await get_token_from_db()
    now = timezone.now()

    if not token:
        return await generate_new_tokens()

    if token.access_expires_at > now:
        return token.access_token

    elif token.refresh_expires_at > now:
        return await refresh_tokens(token.refresh_token)

    else:
        return await generate_new_tokens()
    
#****************************************************
# 2. Get institutions list by country
async def async_get_institutions(token: str, country_code: str = "ES"):
    url = f"{INSTITUTIONS_URL}?country={country_code}"

    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(url, headers=json_headers(token))
        response.raise_for_status()
        return response.json()

# 3. Create an agreement to access bank data
def create_agreement(
    token: str,
    institution_id: str,
    max_days: int = 90,
    valid_days: int = 90,
    access_scope: list = None
):
    if access_scope is None:
        access_scope = ["balances", "details", "transactions"]

    data = {
        "institution_id": institution_id,
        "max_historical_days": str(max_days),
        "access_valid_for_days": str(valid_days),
        "access_scope": access_scope
    }

    response = requests.post(AGREEMENTS_URL, headers=json_headers(token), json=data)
    response.raise_for_status()
    return response.json()

# 4. Create a requisition (start auth process)
def create_requisition(
    token: str,
    redirect_url: str,
    institution_id: str,
    reference: str,
    agreement_id: str,
    user_language: str = "ES"
):
    data = {
        "redirect": redirect_url,
        "institution_id": institution_id,
        "reference": reference,
        "agreement": agreement_id,
        "user_language": user_language
    }

    response = requests.post(REQUISITIONS_URL, headers=json_headers(token), json=data)
    response.raise_for_status()
    return response.json()

# 5. Obté els detalls d'una requisició, incloent els comptes bancaris disponibles.
def get_requisition_details(token: str, requisition_id: str):
    url = f"{REQUISITIONS_URL}{requisition_id}/"
    response = requests.get(url, headers=json_headers(token))
    response.raise_for_status()
    return response.json()

# 6. Retorna les transaccions d'un compte bancari específic mitjançant el seu ID.
def get_account_transactions(token: str, account_id: str):
    url = f"{ACCOUNTS_URL}{account_id}/transactions/"
    response = requests.get(url, headers=json_headers(token))
    response.raise_for_status()
    return response.json()

# 7. Retorna els saldos d’un compte bancari específic mitjançant el seu ID.
def get_account_balance(token: str, account_id: str):
    url = f"{ACCOUNTS_URL}{account_id}/balances/"
    response = requests.get(url, headers=json_headers(token))
    response.raise_for_status()
    return response.json()