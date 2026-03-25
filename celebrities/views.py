from django.shortcuts import render, get_object_or_404, redirect
from .models import Celebrity, Category

def celebrity_list(request):
    stars = Celebrity.objects.all()
    return render(request, 'celebrity_list.html', {'stars': stars})

def celebrity_detail(request, id):
    star = get_object_or_404(Celebrity, id=id)
    return render(request, 'celebrity_detail.html', {'star': star})

def create_celebrity(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        occupation = request.POST.get('occupation')
        bio = request.POST.get('bio')
        Celebrity.objects.create(full_name=full_name, occupation=occupation, bio=bio)
        return redirect('celebrity_list')
    return render(request, 'create_celebrity.html')
