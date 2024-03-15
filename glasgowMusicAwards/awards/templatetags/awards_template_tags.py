from django import template
from awards.models import Vote

register = template.Library()

@register.inclusion_tag('glasgowMusicAwards/artist-page.html')
def get_user_vote(username):
    return {'vote': Vote.objects.filter(user=username)}