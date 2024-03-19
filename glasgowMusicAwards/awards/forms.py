from django import forms
from awards.models import User, Artist, Genre, Comment
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class AddArtistForm(forms.ModelForm):

    #passes in a genre object and displays all the names as a dropdown menu
    genre = forms.ModelChoiceField(queryset=Genre.objects.all(), help_text=mark_safe("Please select the genre the artist belongs in: "))
    artistName = forms.CharField(max_length=128, help_text=mark_safe("<br> Please enter the artists name: "))
    songName = forms.CharField(max_length=128, help_text=mark_safe("<br> Please enter the name of the artists most popular song"))
    songLink = forms.URLField(max_length=200, help_text=mark_safe("<br>Please enter the /embed/ url of their most popular song"))
    votes = forms.CharField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Artist
        fields = ('genre', 'artistName', 'songName', 'songLink',)

class CommentForm(forms.ModelForm):
    
    name = forms.CharField(max_length=128, help_text=mark_safe("<br> Please enter your name: "))
    body = forms.CharField(max_length=500,widget= forms.Textarea, help_text=mark_safe("<br> Write your comment here!"))
    
    class Meta:
        model = Comment
        fields = ('name', 'body',)



