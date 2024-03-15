from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from django.views import View
from django.utils.decorators import method_decorator

from django.contrib.auth.models import User
from awards.models import Genre
from awards.models import Artist , Vote
from awards.forms import UserRegisterForm, AddArtistForm

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
        #Get the username and password given by the user.
        #If value(s) does not exist, it will raise a KeyError exception.
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django given tools to see if the username and password
        # combination is valid - a User object is returned if it is. If it isn't None is returned
        user = authenticate(username=username, password=password)
        if user is None:
            return render(request, 'glasgowMusicAwards/login.html', {'invalid' : True})  

        if user:
            #Must check to see if user account has not been disabled
            if user.is_active:
                #Log the user in and send the user back to the homepage,
                login(request,user)
                return redirect(reverse('awards:index'))
            else:
                #Invalid login details were given so user cannot be logged in.
                print(f"Invalid login details: {username}, {password}")
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
    valid = False
    if request.method == 'POST':
        form = AddArtistForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            valid = True
        else:
            print(form.errors)
    else:
        form = AddArtistForm()

    return render(request, 'glasgowMusicAwards/add_artist.html', {'form': form, 'valid' : valid})

def artistList(request):
    return None
    

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

            vote = Vote(user=user)
            vote.save()

            registered = True
        else:
            #Invalid form or forms - mistakes or something else?
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

        full_user = request.user

        if full_user.is_authenticated:
            vote = Vote.objects.get(user=full_user)
            context_dict['vote'] = vote
        else:
            context_dict[''] = {''}
        
        artist = Artist.objects.get(slug=artist_name_slug)

        genre = Genre.objects.filter(artist__genre__slug=genre_name_slug).first()

        context_dict['artist'] = artist

        context_dict['genre'] = genre

    except Artist.DoesNotExist:

        context_dict['artist'] = None
        context_dict['genre'] = None
        context_dict['vote'] = None

    return render(request, 'glasgowMusicAwards/artist-page.html', context=context_dict)

class VoteButtonView(View):
    @method_decorator(login_required)
    def get(self, request):
        id = request.GET['artistName']
        genre = request.GET['genre']
        username = request.GET['username']
        try:
            artist = Artist.objects.get(artistName=id)
            vote = Vote.objects.get(user=username)

            #Find what genre the user has voted for and set the appropriate boolean to True to prevent
            #them from voting in that category again.
            if genre == "pop":
                vote.popVoted = True
            elif genre == "r&b":
                vote.rbVoted = True
            elif genre == "rap":
                vote.rapVoted = True
            elif genre == "rock":
                vote.rockVoted = True
            elif genre == "country":
                vote.countryVoted = True
            elif genre == "jazz":
                vote.jazzVoted = True
        
            vote.save()

        except Artist.DoesNotExist:
            return HttpResponse(-2)
        except User.DoesNotExist:
            return HttpResponse(-3)
        except ValueError:
            return HttpResponse(-1)
        
        artist.votes = artist.votes + 1
        artist.save()

        return HttpResponse(f"Number of votes: {artist.votes}")
    

    
