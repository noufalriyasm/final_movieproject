from.import views
from django.urls import path
app_name='filmapp'


urlpatterns = [
    path('',views.signup,name="signup"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('login/prod/',views.allProdCat,name="allProdCat"),
    path('<slug:c_slug>/',views.allProdCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:movie_slug>/',views.movieDetail,name='movieCatdetail'),


]
