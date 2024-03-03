from django import template
from awards.models import Artist

register = template.Library()

@register.inclusion_tag('glasgowMusicAwards/genres.html')
def get_artists(current_genre=None):
    artist_list = {}
    all_artists = Artist.objects.all()
    if all_artists:
        for x in range(len(all_artists)):
            if all_artists[x].genre.name == current_genre:
                artist_list["artist"] = all_artists[x]
    return artist_list