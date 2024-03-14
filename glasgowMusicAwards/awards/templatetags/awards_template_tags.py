from django import template
from awards.models import Vote

register = template.Library()

@register.inclusion_tag('glasgowMusicAwards/artist-page.html')
def get_user_vote(user_id):
    return {'vote': Vote.objects.filter(id=int(user_id)).first()}