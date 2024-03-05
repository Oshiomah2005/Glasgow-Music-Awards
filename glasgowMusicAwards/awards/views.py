from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse

from awards.models import Genre
from awards.models import Artist
from glasgowMusicAwards.awards.forms import UserRegisterForm

def index(request):
    response = render(request, 'glasgowMusicAwards/index.html')
    return response

def about(request):
    response = render(request, 'glasgowMusicAwards/about.html')
    return response

def login(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = UserRegisterForm()
    return render(request, 'awards/register.html', {'form': form})

def logout(request):
    response = render(request, 'glasgowMusicAwards/logout.html')
    return response

def addArtist(request):
    response = render(request, 'glasgowMusicAwards/add-artist.html')
    return response

def artistList(request):
    response = render(request, 'glasgowMusicAwards/artist-list.html')
    return response

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('login') 
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def genres(request):
    genre_list = Genre.objects.all()
    response = render(request, 'glasgowMusicAwards/genres.html',{'genre_list': genre_list})
    return response

def artistPage(request):
    response = render(request, 'glasgowMusicAwards/artist-page.html')
    return response

def show_genre(request, genre_name_slug):

    context_dict = {}

    try:
        genre = Genre.objects.get(slug=genre_name_slug)

        artists = Artist.objects.filter(genre=genre)

        context_dict['artists'] = artists

        context_dict['genre'] = genre

    except Genre.DoesNotExist:

        context_dict['genre'] = None
        context_dict['artists'] = None

    return render(request, 'glasgowMusicAwards/artist-list.html', context=context_dict)

def show_artist(request, genre_name_slug , artist_name_slug):

    context_dict = {}

    try:
        artist = Artist.objects.get(slug=artist_name_slug)

        genre = Genre.objects.filter(artist__genre__slug=genre_name_slug)

        context_dict['artist'] = artist

        context_dict['genre'] = genre

    except Artist.DoesNotExist:

        context_dict['artist'] = None
        context_dict['genre'] = None

    return render(request, 'glasgowMusicAwards/artist-page.html', context=context_dict)
    
