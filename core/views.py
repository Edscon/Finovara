from django.shortcuts import render
from django.urls import reverse, NoReverseMatch
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseServerError
from banking_api.views_requests_api import *

def is_superuser(user):
    return user.is_authenticated and user.is_superuser

def get_menu_items():
    
    def safe_reverse(name):
        try:
            return reverse(name)
        except NoReverseMatch:
            return "#"  
    
    return [
        {'name': 'Pricing', 'url': safe_reverse('pricing')},
        {'name': 'Producto', 'url': safe_reverse('producto')},
        {
            'name': 'Recursos',
            'url': '',
            'submenu': [
                {'name': 'Proba1', 'url': safe_reverse('proba1')},
                {'name': 'Proba2', 'url': safe_reverse('proba2')}
            ]
        },
        {
            'name': 'About',
            'url': '',
            'submenu': [
                {'name': 'Proba1', 'url': safe_reverse('proba1')},
                {'name': 'Proba2', 'url': safe_reverse('proba2')}
            ]
        },
    ]

def frontpage(request):

    menu_items = get_menu_items()

    context = {
        'menu_items': menu_items,
        'proba': 'Proba',
    }

    return render(request, 'corehtml/frontpage.html', context)




### Authentication and Authorization Views ###
@user_passes_test(is_superuser)
def auth_manager(request):
    menu_items = get_menu_items()
    context = { 'menu_items': menu_items, }
    return render(request, 'corehtml/auth_manager.html', context)

@csrf_exempt
async def update_institutions(request):
    try:
        access_key = await get_valid_access_token()
        institutions = await async_get_institutions(access_key, 'es')

        # Guardem amb sync_to_async i await
        for item in institutions:
            await save_institution(item)

        return JsonResponse(institutions, safe=False)
    except requests.RequestException as e:
        return HttpResponseServerError(f"Error obtenint institucions: {str(e)}")
