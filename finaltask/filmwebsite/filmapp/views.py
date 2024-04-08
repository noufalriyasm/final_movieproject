from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category,Movie
from django.db.models import Avg
# from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator,EmptyPage,InvalidPage
# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('prod/')
        else:
            messages.info(request,"Invalid User")
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')


def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email=request.POST['email']
        password = request.POST['password']
        cpassword=request.POST['password1']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exist")
                return redirect('/')

            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already exist")
                return redirect('/')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                user.save();
                messages.info(request,"User Created Succesfully")
                return redirect('login/')


        else:
            messages.info(request,"Password Verification failed")
            return redirect('/')
        return redirect('/')





    return render(request,"signup.html")


# def home(request):
#
#     return render(request,"error.html")


# def profile(request):
#     return render(request,"profile.html")


def allProdCat(request,c_slug=None):
    c_page=None
    movies=None
    if c_slug !=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        movies=Movie.objects.all().filter(category=c_page,available_to_watch=True)
    else:
        movies = Movie.objects.all().filter(available_to_watch=True)
        # paginator = Paginator(movies_list, 2)
        # try:
        #     page = int(request.GET.get('page', '1'))
        # except:
        #     page = 1
        # try:
        #     movies = paginator.page(page)
        # except (EmptyPage, InvalidPage):
        #     movies = paginator.page(paginator.num_pages)

    return render(request, "category.html", {'category': c_page, 'movies':movies})


def movieDetail(request,c_slug,movie_slug):
    try:
        movie=Movie.objects.get(category__slug=c_slug,slug=movie_slug)
    except Exception as e:
        raise e
    return render(request,'movie.html',{'movie':movie})




# def submit_review(request,movie_id):
#     url=request.META.get('HTTP_REFERER')
#     if request.method=='POST':
#         try:
#             reviews=ReviewRating.objects.get(user__id=request.user.id,movie__id=movie_id)
#             form=ReviewForm(request.POST,instance=reviews)
#             form.save()
#             messages.success(request,"Thankyou,Review is Updated")
#             return redirect('url')
#         except ReviewRating.DoesNotExist:
#             form=ReviewForm(request.POST)
#             if form.is_valid():
#                 data=ReviewRating()
#                 data.rating=form.cleaned_data['rating']
#                 data.rating=form.cleaned_data['review']
#                 data.movie_id=movie_id
#                 data.user_id=request.user.id
#                 data.save()
#                 messages.success(request,"Thankyou, Review is Submitted")




# def view_profile(request):
#     profile=request.user
#     return render(request,"profile.html",{'profile':profile})
#
#
# def edit_profile(request):
#     if request.method=='POST':
#         form=ProfileForm(request.POST,instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('view_profile')
#     else:
#         form=ProfileForm(instance=request.user)
#     return render(request,"edit_profile.html",{'form':form})


# def add_rating(request,movie_id):
#     movie=get_object_or_404(Movie,pk=movie_id)
#     if request.method=='POST':
#         rating_form=RatingForm(request.POST)
#         if rating_form.is_valid():
#             rating=rating_form.save(commit=False)
#             rating.movie=movie
#             rating.user=request.user
#             rating.save()
#             return redirect('/',movie_id=movie_id)
#     else:
#         rating_form=RatingForm()
#
#     return render(request,"rating.html",{'movie':movie,'rating_form':rating_form})
#
#
# def add_comment(request,movie_id):
#     movie=get_object_or_404(Movie,pk=movie_id)
#     if request.method=='POST':
#         comment_form=CommentForm(request.POST)
#         if comment_form.is_valid():
#             comment=comment_form.save(commit=False)
#             comment.movie=movie
#             comment.user=request.user
#             comment.save()
#             return redirect('/',movie_id=movie_id)
#
#     else:
#         comment_form=CommentForm()
#     return redirect(request,"comment.html",{'movie':movie,'comment_form':comment_form})
