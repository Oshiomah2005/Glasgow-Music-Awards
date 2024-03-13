from django.urls import path
from awards import views
from django.contrib.auth.views import LoginView, LogoutView
app_name = 'awards'

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('login/', views.login, name='login'),
    path("register/", views.register, name="register"),
    path("genres/", views.genres, name="genres"),
    #Changed line below from path("genres/<slug:genre_name_slug>/artist-list/",views.artistList, name="artist-list")
    path("genres/<slug:genre_name_slug>/artist-list/", 
         views.show_genre, name="show_genre"),
    path("genres/<slug:genre_name_slug>/artist-list/<slug:artist_name_slug>/artist-page/",
        views.show_artist, name="show_artist"),
    path("add-artist/", views.addArtist, name="add-artist"),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
