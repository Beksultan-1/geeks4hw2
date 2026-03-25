from django.shortcuts import render, get_object_or_404
from .models import Celebrity

def celebrity_list(request):
    celebrities = Celebrity.objects.all()
    return render(request, 'celebrity_list.html', {'celebrities': celebrities})

def celebrity_detail(request, id):
    star = get_object_or_404(Celebrity, id=id)
    return render(request, 'celebrity_detail.html', {'star': star})
