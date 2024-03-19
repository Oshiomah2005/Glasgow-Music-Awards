import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "glasgowMusicAwards.settings")
import django
django.setup()
from django.db import IntegrityError
from awards.models import *

        
def populate():    
    
    #Define artists categorised by genres
    pop = [
        {"name": "Ariana Grande", "slug":"ariana-grande", "songName": "7 Rings", "votes":4, "link": "https://www.youtube.com/embed/QYh6mYIJG2Y?si=UG-1Tbi8GSnFixd4",},
        {"name": "Dua Lipa", "slug":"dua-lipa", "songName": "Don't Start Now", "votes":0, "link": "https://www.youtube.com/embed/oygrmJFKYZY?si=zsILU4OJWHSGuvmd",},
        {"name": "Taylor Swift","slug":"taylor-swift", "songName": "Blank Space", "votes":0, "link": "https://www.youtube.com/embed/e-ORhEE9VVg?si=e_sEuP29glVFOS2V",},
        {"name": "Ed Sheeran","slug":"ed-sheeran", "songName": "Shape of You", "votes":0, "link": "https://www.youtube.com/embed/JGwWNGJdvx8?si=C84eDlTUE7EG2jWa",},
        {"name": "Billie Eilish", "slug": "billie-eilish" , "songName": "Lovely", "votes":0, "link": "https://www.youtube.com/embed/V1Pl8CzNzCw?si=NVL6DKs9eg7QVb-4",},
        ]
    rb = [
        {"name": "Frank Ocean", "slug":"frank-ocean","songName": "Nights", "votes":4, "link": "https://www.youtube.com/embed/r4l9bFqgMaQ?si=W6B0yIpB1eZLCwtC",},
        {"name": "Maxwell", "slug":"maxwell", "songName": "Pretty Wings", "votes":0, "link": "https://www.youtube.com/embed/RkPy4yq7EJo?si=C-AHn2y6oy_ZyE_v",},
        {"name": "D'Angelo" , "slug":"dangelo", "songName": "Lady", "votes":0, "link": "https://www.youtube.com/embed/YBB8valskCQ?si=2GDiekiNgIhGKz5h",},
        {"name": "Usher", "slug":"usher","songName": "Yeah!", "votes":0, "link": "https://www.youtube.com/embed/GxBSyx85Kp8?si=5c-euF-R6SxwDpw2",},
        {"name": "Erykah Badu", "slug":"erykah-badu","songName": "On & On", "votes":0, "link": "https://www.youtube.com/embed/-CPCs7vVz6s?si=EwYNpW6Grfz8t_bs",}
        ]
    rap = [
        {"name": "Eminem", "slug":"eminem","songName": "Crack A Bottle", "votes":4, "link": "https://www.youtube.com/embed/_wN3wl473M0?si=VhgS5ehNjhDqK1xG",},
        {"name": "J Cole", "slug":"j-cole","songName": "No Role Modelz", "votes":0, "link": "https://www.youtube.com/embed/0EnRK5YvBwU?si=HAkFAo_8pESHuekg",},
        {"name": "Juice Wrld", "slug":"juice-wrld","songName": "Lucid Dreams", "votes":0, "link": "https://www.youtube.com/embed/mzB1VGEGcSU?si=HXyjloVD5q25RHqV",},
        {"name": "Queen Latifah", "slug":"queen-latifah","songName": "U.N.I.T.Y", "votes":0, "link": "https://www.youtube.com/embed/f8cHxydDb7o?si=QHTOQcBcO_jYyWdc",},
        {"name": "Megan Thee Stallion", "slug":"megan-thee-stallion","songName": "Hiss", "votes":0, "link": "https://www.youtube.com/embed/XVgCLQ_JQfU?si=bOvolmEaxPWCdY95",},
        ]
    rock = [
        {"name": "Guns N'Roses","slug":"guns-n-roses", "songName": "Sweet Child O' Mine", "votes":4, "link": "https://www.youtube.com/embed/1w7OgIMMRc4?si=mtePE5Pzy9Xm3pRK",},
        {"name": "Zach Bryan","slug":"zach-bryan", "songName": "Condemned", "votes":0, "link": "https://www.youtube.com/embed/PhuoyEQYyx8?si=FKH_ZSTxoaVLM0cz",},
        {"name": "Jelly Roll", "slug":"jelly-roll","songName": "Son of a Sinner", "votes":0, "link": "https://www.youtube.com/embed/n4Z1cpdkgQU?si=ToGV3i_MbCaW_QiS",},
        {"name": "Imagine Dragons", "slug":"imagine-dragons","songName": "Radioactive", "votes":0, "link": "https://www.youtube.com/embed/ktvTqknDobU?si=V8HA5UhxhnVo5Gts",},
        {"name": "Fleetwood Mac", "slug":"fleetwood-mac","songName": "Dreams", "votes":0, "link": "https://www.youtube.com/embed/Y3ywicffOj4?si=EVLCrxoRZn-cDJzz",},
        ]
    country = [
        {"name": "Shania Twain", "slug":"shania-twain","songName": "Man! I feel Like a Woman", "votes":4, "link": "https://www.youtube.com/embed/ZJL4UGSbeFg?si=kOCHE3kX2LybeXZv",},
        {"name": "John Denver", "slug":"john-denver","songName": "Take Me Home, Country Roads", "votes":0, "link": "https://www.youtube.com/embed/1vrEljMfXYo?si=r8s2DHCnfaSFlMPB",},
        {"name": "Carrie Underwood", "slug":"carrie-underwood","songName": "Before He Cheats", "votes":0, "link": "https://www.youtube.com/embed/WaSy8yy-mr8?si=PN2TdMYGbGCEvGSz",},
        {"name": "Alison Krauss", "slug":"alison-krauss","songName": "Baby Mine", "votes":0, "link": "https://www.youtube.com/embed/kCjhm-qLERQ?si=CDPOKsHiEKxWpETm",},
        {"name": "Lucinda Williams", "slug":"lucinda-williams","songName": "Car Wheels on a Gravel Road", "votes":0, "link": "https://www.youtube.com/embed/7tUzhodl_rw?si=h6aqbzhuEndLyL5d",},
        ]
    jazz = [
        {"name": "Billie Holiday", "slug":"billie-holiday","songName": "Strange Fruit", "votes":4, "link": "https://www.youtube.com/embed/Web007rzSOI?si=e5reh65i2HeUEy3n",},
        {"name": "Ella Fitzgerald", "slug":"ella-fitzgerald","songName": "Cry Me a River", "votes":0, "link": "https://www.youtube.com/embed/wSw8KaZIzYg?si=kRJXDp5pJpwkhOGP",},
        {"name": "Duke Ellington", "slug":"duke-ellington","songName": "Don't Get Around Much Anymore", "votes":0, "link": "https://www.youtube.com/embed/yxwvOncHVbQ?si=fUMBdHEPSVJ0xpiT",},
        {"name": "Louis Armstrong", "slug":"louis-armstrong","songName": "What a Wonderful World", "votes":0, "link": "https://www.youtube.com/embed/rBrd_3VMC3c?si=Dh4BF1VJzMrPClHs",},
        {"name": "John Coltrane", "slug":"john-coltrane","songName": "India", "votes":0, "link": "https://www.youtube.com/embed/tiJI9hBBdS8?si=mnZOFRWc6KDuADp5",},
        ]
    
    # Define a dictionary mapping genre names to their corresponding list of artists
    genres = {"Pop":{"genreId":0,"name":pop, "slug":'pop'},
              "R&B":{"genreId":1,"name":rb, "slug":'rb'},
              "Rap":{"genreId":2, "name":rap, "slug":'rap'},
              "Rock":{"genreId":3,"name":rock, "slug":'rock'},
              "Country":{"genreId":4,"name":country, "slug":'country'},
              "Jazz":{"genreId":5,"name":jazz, "slug":'jazz'},
              }
    # Iterate over each genre and its associated list of artists
    for genre, genre_data in genres.items():
        #Create or get genre object
        g = add_genre(genre_data["genreId"], genre, genre_data["slug"])
        # Iterate over each artist in the genre
        for a in genre_data["name"]:
            # Create or get Artist object and set its attributes
            addArtist(g, a["name"], a["songName"], a["link"], a["votes"], a["slug"])
            
    # Print all genres and associated artists
    for g in Genre.objects.all():
        for a in Artist.objects.filter(genre=g):
            print(f"-{g}: {a}")

# Function to create or get genre
def add_genre(id, name, slug):
    try:
        # Try to get the genre from the database by slug
        print(slug)
        g = Genre.objects.get(slug=slug)
        print(f'Genre "{name}" already exists.')
    except Genre.DoesNotExist:
        # If the genre doesn't exist, create it
        print("hi")
        g = Genre.objects.create(genreId=id, name=name, slug=slug)
        print(f'Genre "{name}" created.')
    return g

# Function to create or get an Artist object
def addArtist(genre, name, songName, link, votes, slug):
    try:
        # Try to get the genre from the database by slug
        a = Artist.objects.get(slug=slug)
        print(f'Artist "{name}" already exists.')
    except Artist.DoesNotExist:
        # If the genre doesn't exist, create it
        a = Artist.objects.create(genre=genre, artistName=name, songName=songName, songLink = link, votes = votes)
        print(f'Artist "{name}" in genre "{genre.name}" created.')
    return a

if __name__ == "__main__":
    print("Starting population script...")
    populate()