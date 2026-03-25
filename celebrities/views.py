from django.shortcuts import render
from .models import Celebrity

def celebrity_list(request):
    celebrities = Celebrity.objects.all()
    return render(request, 'celebrity_list.html', {'celebrities': celebrities})
