from django.urls import path
from awards import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'awards'

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('login/', views.user_login, name='login'),
    path("register/", views.register, name="register"),
    path("genres/", views.genres, name="genres"),
    path("genres/<slug:genre_name_slug>/artist-list/", 
         views.show_genre, name="show_genre"),
    path("add_artist/", views.addArtist, name="add_artist"),
    path('logout/', views.user_logout, name='logout'),
    path('vote_artist/', views.VoteButtonView.as_view(), name = 'vote_artist'),
    path('awards/genres/<slug:genre_slug>/artist-list/<slug:artist_name_slug>/artist-page/', 
        views.artist_detail, name='artist_detail')
]
