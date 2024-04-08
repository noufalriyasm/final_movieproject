from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from filmapp.models import Movie
from .forms import MovieForm

# Create your views here.
# def add_movie(request):
#
#     if request.method=='POST':
#         name=request.POST.get('name')
#         description = request.POST.get('description')
#
#         actors = request.POST.get('actors')
#         released = request.POST.get('released')
#         link= request.POST.get('link')
#
#         movie=Movie(name=name,description=description,actors=actors,released=released,link=link)
#         movie.save()
#     return render(request,"add.html")

def add_movie(request):
    url = request.META.get('HTTP_REFERER')
    if request.method=='POST':
        form=MovieForm(request.POST,request.FILES)
        if form.is_valid():
            movie=form.save(commit=False)
            movie.added_by=request.user
            movie.save()
            messages.success(request,"Movie Addedd Succesfully")
        return redirect(url)
    else:
        form=MovieForm()
        return render(request,"add.html",{'form':form})


def edit_movie(request, movie_id):
    url = request.META.get('HTTP_REFERER')
    movie = get_object_or_404(Movie, pk=movie_id)
    if movie.added_by != request.user:
        # messages.warning(request, "Sorry.. You have no access to edit it")
        return redirect(url)
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            messages.success(request,"Updated Succesfully")
            return redirect(url)
    else:
        form = MovieForm(instance=movie)
    return render(request, 'edit_movie.html', {'form': form, 'movie': movie})


def delete_movie(request, movie_id):
    url = request.META.get('HTTP_REFERER')
    movie = get_object_or_404(Movie, id=movie_id)
    if request.user != movie.added_by:
        # messages.warning(request,"Sorry.. You have no access to delete it")
        return redirect(url)
    if request.method == 'POST':
        movie.delete()
        return redirect('/')

    return render(request, 'delete_movie.html', {'movie': movie})