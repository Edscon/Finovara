from django.shortcuts import render

# Create your views here.
def frontpage(request):
    
    context = {
        'proba': 'Proba',

    }

    return render(request, 'corehtml/frontpage.html', context)