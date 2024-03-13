from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from awards.models import Genre
from awards.models import Artist
from awards.forms import UserRegisterForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    response = render(request, 'glasgowMusicAwards/index.html')
    return response

def about(request):
    response = render(request, 'glasgowMusicAwards/about.html')
    return response

def user_login(request):
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        #Get the username, email, and password given by the user.
        #If value(s) does not exist, it will raise a KeyError exception.
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Use Django given tools to see if the username, email, and password
        # combination is valid - a User object is returned if it is. If it isn't None is returned
        user = authenticate(username=username, email=email, password=password)

        if user:
            #Must check to see if user account has not been disabled
            if user.is_active:
                #Log the user in and send the user back to the homepage,
                login(request,user)
                return redirect(reverse('awards:index'))
            else:
                #Invalid login details were given so user cannot be logged in.
                print(f"Invalid login details: {username}, {email}, {password}")
                return HttpResponse("Invalid login details supplied.")
    #Request is not POST, so display the login form to user.
    else:
        return render(request, 'glasgowMusicAwards/login.html')  

@login_required
def user_logout(request):
    # Logout the user.
    logout(request)
    # Take the user to the logout page.
    response = render(request, 'glasgowMusicAwards/logout.html')
    return response

@login_required
def addArtist(request):
    response = render(request, 'glasgowMusicAwards/add-artist.html')
    return response

def artistList(request):
    response = render(request, 'glasgowMusicAwards/artist-list.html')
    return response

def register(request):
    #Describes to template if registration was successful.
    registered = False

    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            #Save user's form data to database.
            user = user_form.save()

            #Hash password with the set_password method.
            #When hashed, update the user object.
            user.set_password(user.password)
            user.save()

            registered = True
        else:
            #Invaid form or forms - mistakes or something else?
            #Print problems to the terminal.
            print(user_form.errors)
    else:
        #Not a HTTP POST, so render the form.
        #These forms will be blank, ready for user input.
        user_form = UserRegisterForm()
    return render(request, 'glasgowMusicAwards/register.html', {'user_form': user_form, 'registered': registered})

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

        #finds the top artist in a category
        top_artist = "No top artist yet as no votes have been made"
        most_votes = 0
        for x in range(len(artists)):
            num_votes = artists[x].votes
            if num_votes > most_votes:
                most_votes = num_votes
                top_artist = artists[x].artistName

        context_dict['artists'] = artists

        context_dict['genre'] = genre

        context_dict['top_artist'] = top_artist

    except Genre.DoesNotExist:

        context_dict['genre'] = None
        context_dict['artists'] = None
        context_dict['top_artist'] = None

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
    
