from django.shortcuts import render
from mApp.models import Movie
from mApp.form import MovieForm

# Create your views here.
def display(request):
    return render(request,'htmlPage/index.html')
def display_movie(request):
    movie_list=Movie.objects.all()
    return render(request,'htmlPage/movielist.html',{'mlist':movie_list})
def add_movie(request):
    form=MovieForm()
    if request.method=='POST':
        form=MovieForm(request.POST)
        if form.is_valid():
            form.save()
        return display(request)
    return render(request,'htmlPage/addmovie.html',{'amovie':form})
