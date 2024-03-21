from django.contrib import admin
from awards.models import UserProfile, Post, Comment, Genre, Artist, Vote

admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(Vote)

    