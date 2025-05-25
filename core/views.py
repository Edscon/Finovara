from django.shortcuts import render
from django.urls import reverse, NoReverseMatch



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

# Create your views here.
def frontpage(request):

    menu_items = get_menu_items()

    context = {
        'menu_items': menu_items,
        'proba': 'Proba',
    }

    return render(request, 'corehtml/frontpage.html', context)