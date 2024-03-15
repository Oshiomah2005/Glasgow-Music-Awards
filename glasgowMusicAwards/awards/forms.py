from django import forms
from awards.models import User
from django.contrib.auth.models import User

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

from django import forms
from awards.models import Artist, Genre
from django.contrib.auth.models import User

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class AddArtistForm(forms.ModelForm):

    genre = forms.ModelChoiceField(queryset=Genre.objects.all())
    artistName = forms.CharField(max_length=128, help_text="Please enter the artists name")
    songName = forms.CharField(max_length=128, help_text="enter the name of the artists most popular song")
    songLink = forms.URLField(max_length=200, help_text="Please enter the url of their most popular song")
    votes = forms.CharField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Artist
        fields = ('genre', 'artistName', 'songName', 'songLink',)


