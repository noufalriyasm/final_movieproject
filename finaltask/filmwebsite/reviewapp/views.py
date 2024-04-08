from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from filmapp.models import Movie
from .models import Review,Rating
from .forms import RatingForm, ReviewForm

# def movie_detail(request, movie_id):
#     movie = get_object_or_404(Movie, pk=movie_id)
#     ratings = movie.ratings.all()
#     reviews = movie.reviews.all()
#     return render(request, 'movie_detail.html', {'movie': movie, 'ratings': ratings, 'reviews': reviews})

# def add_rating(request, movie_id):
#     url = request.META.get('HTTP_REFERER')
#     task = Rating.objects.all()
#     movie = get_object_or_404(Movie, pk=movie_id)
#     if request.method == 'POST':
#
#         form = RatingForm(request.POST)
#         if form.is_valid():
#             rating = form.save(commit=False)
#             rating.movie = movie
#             rating.user = request.user
#             rating.save()
#             messages.success(request, "Succesfully Submitted Your Rating")
#
#             return redirect(url, movie_id=movie_id)
#
#     else:
#         form = RatingForm()
#     return render(request, 'rating.html', {'form': form,'task':task})


def add_rating(request, movie_id):
    url = request.META.get('HTTP_REFERER')
    movie = get_object_or_404(Movie, pk=movie_id)
    task = Rating.objects.all()
    user = request.user
    if Rating.objects.filter(movie=movie, user=user).exists():
        # User has already rated, update the rating
        rating = Rating.objects.get(movie=movie, user=user)
        if request.method == 'POST':
            form = RatingForm(request.POST, instance=rating)
            if form.is_valid():
                form.save()
                messages.success(request,"Your Rating is Updated")
                return redirect(url)
        else:
            form = RatingForm(instance=rating)
    else:
        # User has not rated yet, create new rating
        if request.method == 'POST':
            form = RatingForm(request.POST)
            if form.is_valid():
                rating = form.save(commit=False)
                rating.movie = movie
                rating.user = user
                rating.save()
                messages.success(request,"Your Rating is Saved")
                return redirect(url)
        else:
            form = RatingForm()
    return render(request, 'rating.html', {'form': form,'task':task})



def add_review(request, movie_id):
    url = request.META.get('HTTP_REFERER')
    task1 = Review.objects.all()
    movie = get_object_or_404(Movie, pk=movie_id)

    user = request.user
    if Review.objects.filter(movie=movie, user=user).exists():
        # User has already reviewed, update the rating
        review = Review.objects.get(movie=movie, user=user)
        if request.method == 'POST':
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
                form.save()
                messages.success(request,"Your Review is Updated")
                return redirect(url)
        else:
            form = ReviewForm(instance=review)
    else:
        # User has not rated yet, create new rating
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.movie = movie
                review.user = user
                review.save()
                messages.success(request,"Your Review is Saved")
                return redirect(url)
        else:
            form = ReviewForm()
    return render(request, 'rating.html', {'form': form,'task1': task1})

# def add_review(request, movie_id):
#     url = request.META.get('HTTP_REFERER')
#     movie = get_object_or_404(Movie, pk=movie_id)
#     existing_review = Review.objects.filter(movie=movie, user=request.user).first()
#
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             if existing_review:
#                 existing_review.review_text = form.cleaned_data['review_text']
#                 existing_review.save()
#             else:
#                 review = form.save(commit=False)
#                 review.movie = movie
#                 review.user = request.user
#                 review.save()
#                 messages.success(request,"Your Review is Updated")
#
#             return redirect(url, movie_id=movie_id)
#     else:
#         initial_data = {'text': existing_review.review_text if existing_review else ''}
#         form = ReviewForm(initial=initial_data)
#
#     return render(request, 'review.html', {'form': form})





# def add_review(request, movie_id):
#     url = request.META.get('HTTP_REFERER')
#     reviews = Review.objects.all()
#     movie = get_object_or_404(Movie, pk=movie_id)
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             review = form.save(commit=False)
#             review.movie = movie
#             review.user = request.user
#             review.save()
#             messages.success(request,"Successful")
#             return redirect(url, movie_id=movie_id)
#     else:
#         form = ReviewForm()
#     return render(request, 'review.html', {'form': form,'reviews':reviews})


# Create your views here.
