from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    CHAR_LENGTH = 128
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    userId = models.IntegerField(unique=True)
    name = models.CharField(max_length=CHAR_LENGTH, unique=True)
    email = models.CharField(max_length=CHAR_LENGTH, unique=True)
    password = models.CharField(max_length=CHAR_LENGTH)
    role = models.CharField(max_length=CHAR_LENGTH)
    
    def __str__(self):
        return self.user.username
    
class Post(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    
    postContent = models.CharField(max_length=255)
    
    def __str__(self):
        return self.postContent
    
class Comment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    
    contentComment = models.CharField(max_length=255)
    commentedAt = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.contentComment
    
class Genre(models.Model):
    genreId = models.IntegerField(unique=True)
    name = models.CharField(max_length=128, unique=True)
    
    slug = models.SlugField(unique =  True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Genre, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
class Artist(models.Model):
    CHAR_LENGTH = 128
    
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    
    artistName = models.CharField(max_length=CHAR_LENGTH, unique=True)
    
    votes = models.ManyToManyField('Vote', related_name='artists')
    
    slug = models.SlugField(unique =  True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.artistName)
        super(Artist, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.artistName
    
    
class Vote(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
   
    popVoted = models.BooleanField(default=False)
    rbVoted = models.BooleanField(default=False)
    rapVoted = models.BooleanField(default=False)
    rockVoted = models.BooleanField(default=False)
    countryVoted = models.BooleanField(default=False)
    jazzVoted = models.BooleanField(default=False)
    
class Content(models.Model):
    
    CHAR_LENGTH = 128
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    
    artistName = models.CharField(max_length=128)
    most_popular_song = models.CharField(max_length=CHAR_LENGTH)
    songLink = models.URLField()
    
    def __str__(self):
        return self.artistName