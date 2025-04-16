from django.shortcuts import render
from keys.models import ApiKey

# Create your views here.
def frontpage(request):

    context = {
        'proba': 'Proba',
    }

    return render(request, 'corehtml/frontpage.html', context)