from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from .models import Movie

def home(request) :
    movie = Movie.objects.all()
    sort = request.GET.get('sort','')
    if sort == 'name':
        movie = Movie.objects.all().order_by('name')
    if sort == 'pub_date':
        movie = Movie.objects.all().order_by('pub_date')
    if sort == 'rank':
        movie = Movie.objects.all().order_by('rank')
    q = request.GET.get('q','')
    if q:
        movie = movie.filter(name__icontains=q)
    paginator = Paginator(movie, 3)
    page = request.GET.get('page')
    movie = paginator.get_page(page)
    
    return render(request, 'home.html', {'movies' : movie, 'q':q})

def create(request) :
    if request.method == 'POST' :
        movie = Movie()
        movie.name = request.POST['name']
        movie.grade = request.POST['grade']
        movie.pub_date = request.POST['pub_date']
        movie.running_time = request.POST['running_time']
        movie.category = request.POST['category']
        movie.rank = request.POST['rank']
        movie.image = request.FILES.get('image')
        movie.save()
        return redirect('home')
    return render(request, 'create.html')

def edit(request, id) :
    movie = get_object_or_404(Movie, pk = id)
    if request.method == 'POST' :
        movie.name = request.POST['name']
        movie.grade = request.POST['grade']
        movie.pub_date = request.POST['pub_date']
        movie.running_time = request.POST['running_time']
        movie.category = request.POST['category']
        movie.rank = request.POST['rank']
        if request.POST.get('img_change') is not None : # 포스터 사진 변경 여부
            movie.image = request.FILES.get('image')
        movie.save()
        return redirect('home')
    return render(request, 'edit.html', {'movie' : movie})

def delete(request, id) :
    movie = get_object_or_404(Movie, pk = id)
    movie.delete()
    return redirect('home')
