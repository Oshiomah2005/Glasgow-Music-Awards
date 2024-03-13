import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')

import django
django.setup()
from awards.models import *

def populate():
    user_profiles = [
        {
            'userId': 'paul',
            'name': 'paulm',
            'email': 'email@email',
            'password': 'vbfvb',
            'role': 'user'
        }
    ]

    post = [
        {
            'user': 'paul',
            'postContent': 'detail of post content'
        }
    ]

    comment = [
        {
            'user': 'paul',
            'contentComment': 'detail of content comment'
        }
    ]

    genre = [
        {
            'genreId': '01',
            'name': 'Michael Jackson',
            'slug': 'michael-jackson'
        }
    ]

    artist = [
        {
            'genre': 'pop',
            'artistName': 'Michael Jackson',
            'vote': 'detail of vote',
            'slug': 'michael-jackson'
        }
    ]

    vote = [
        {
            'user': 'paul',
            'artist': 'Michael Jackson'
        }
    ]

    content = [
        {
            'genre': 'pop',
            'artist': 'Michael Jackson',
            'artistName': 'Michael Jackson',
            'most_popular_song': 'Billie Jean',
            'songLink': 'http://link/'
         }
    ]

    for user in user_profiles:
        p = addUser(user['userId'])

    for post in Post:
        userProfile = UserProfile.objects.get(name=post['user'])
        p = addPost(userProfile, post['postContent'])

    for comment in Comment:
        userProfile = UserProfile.objects.get(name=comment['user'])
        c = addComment(userProfile, comment['contentComment'])

    for genre in Genre:
        g = addGenre(genre['genreId'], genre['name'])

    for artist in Artist:
        genre = Genre.objects.get(genreId=artist['genre'])
        a = addArtist(genre, artist['artistName'])

def addUser(userId, name, email, password, role):
    user = UserProfile.objects.get_or_create(username=name, email=email)[0]
    user.set_password(password)
    user.save()

    profile, created = UserProfile.objects.get_or_create(user=user, userId=userId,
                                                          defaults={'name': name, 'email': email,
                                                                    'password': password, 'role': role})
    return profile


def addPost(userProfile, postContent):
    post, created = Post.objects.get_or_create(user=userProfile, postContent=postContent)
    return post

def addComment(userProfile, contentComment):
    comment, created = Comment.objects.get_or_create(user=userProfile, contentComment=contentComment)
    return comment

def addGenre(genreId, name):
    genre, created = Genre.objects.get_or_create(genreId=genreId, name=name)
    return genre

def addArtist(genre, artistName):
    artist, created = Artist.objects.get_or_create(genre=genre, artistName=artistName)
    return artist

def addVote(userProfile, artist, popVoted=False, rbVoted=False, rapVoted=False, rockVoted=False, countryVoted=False, jazzVoted=False):
    vote, created = Vote.objects.get_or_create(user=userProfile, artist=artist,
                                               defaults={'popVoted': popVoted, 'rbVoted': rbVoted,
                                                         'rapVoted': rapVoted, 'rockVoted': rockVoted,
                                                         'countryVoted': countryVoted, 'jazzVoted': jazzVoted})
    return vote

def addContent(genre, artist, artistName, most_popular_song, songLink):
    content, created = Content.objects.get_or_create(genre=genre, artist=artist,
                                                     defaults={'artistName': artistName,
                                                               'most_popular_song': most_popular_song,
                                                               'songLink': songLink})
    return content


if __name__ == '__main__':
    print('Starting population script...')
    populate()