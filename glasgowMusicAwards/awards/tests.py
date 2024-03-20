from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

from awards.models import Genre, Artist, Vote
from awards.forms import AddArtistForm, UserRegisterForm

# Create your tests here.

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='test', password='password')
        self.genre1 = Genre.objects.create(name="Pop", genreId=1, slug="pop")
        self.genre2 = Genre.objects.create(name="Rap", genreId=2, slug="rap")
        self.genre3 = Genre.objects.create(name="Rock", genreId=3, slug="rock")
        self.genre4 = Genre.objects.create(name="R&B", genreId=4, slug="rnb")
        self.genre5 = Genre.objects.create(name="Country", genreId=5, slug="country")
        self.genre6 = Genre.objects.create(name="Jazz", genreId=6, slug="jazz")
        self.list_genres = {self.genre1, self.genre2, self.genre3, self.genre4, self.genre5, self.genre6}
        self.artist1 = Artist.objects.create(artistName='Artist 1', genre=self.genre1, votes=10, slug='artist-1')
        self.artist2 = Artist.objects.create(artistName='Artist 2', genre=self.genre1, votes=5, slug='artist-2')

    def test_index(self):
        response = self.client.get(reverse('awards:index'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'glasgowMusicAwards/index.html')

    def test_about(self):
        response = self.client.get(reverse('awards:about'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'glasgowMusicAwards/about.html')

    def test_user_login_unsuccessful(self):
        self.client.logout()
        response = self.client.post(reverse('awards:login'), {'username': 'invalidusername', 'password': 'invalidpassword'})
        self.assertEquals(response.status_code, 200)
        self.assertFalse(response.wsgi_request.user.is_authenticated)
        self.assertTemplateUsed(response, 'glasgowMusicAwards/login.html')

    def test_user_login_successful(self):
        response = self.client.post(reverse('awards:login'), {'username': self.user.username, 'password': self.user.password})
        self.assertEquals(response.status_code,200)
        self.assertTrue(self.user.is_authenticated)
    
    def test_user_logout(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('awards:logout'))
        self.assertEquals(response.status_code, 302)
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_add_artist(self):
        response = self.client.post(reverse('awards:add_artist'))
        self.assertEquals(response.status_code, 302)

    def test_register_post_valid_data(self):
        valid_form_data = {
            'username': 'testuser',
            'password': 'testpassword',
        }

        response = self.client.post(reverse('awards:register'), valid_form_data)
        self.assertTemplateUsed(response, 'glasgowMusicAwards/register.html')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['user_form'], UserRegisterForm)
        self.assertTrue(User.objects.filter(username='testuser').exists())
        self.assertTrue(Vote.objects.filter(user__username='testuser').exists())
    
    
    def test_register_post_invalid_data(self):
        invalid_form_data = {
        }

        response = self.client.post(reverse('awards:register'), invalid_form_data)
        self.assertTemplateUsed(response, 'glasgowMusicAwards/register.html')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['registered'])
        self.assertIsInstance(response.context['user_form'], UserRegisterForm)
        self.assertTrue(response.context['user_form'].errors)


    def test_genres(self):
        response = self.client.get(reverse('awards:genres'), {'genre_list' : self.list_genres})
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'glasgowMusicAwards/genres.html')

        for genre in self.list_genres:
            self.assertContains(response, genre.name)

    def test_show_genre(self):
        response = self.client.get(reverse('awards:show_genre', args=[self.genre1.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['genre'], self.genre1)
        self.assertQuerysetEqual(response.context['artists'].order_by('id'), [repr(self.artist1), repr(self.artist2)])
        self.assertEqual(response.context['top_artist'], self.artist1.artistName)
        self.assertTemplateUsed(response,'glasgowMusicAwards/artist-list.html')

    def test_show_artist(self):
        response = self.client.get(reverse('awards:artist_detail', args=[self.genre1.slug, self.artist1.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['artist'], self.artist1)
        self.assertEqual(response.context['genre'], self.genre1)
        self.assertTemplateUsed(response,'glasgowMusicAwards/artist-page.html')

class VoteButtonViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.vote = Vote.objects.create(user=self.user)
        self.client.login(username='testuser', password='testpassword')
        self.genre = Genre.objects.create(name="Jazz", genreId=6, slug="jazz")
        self.artist = Artist.objects.create(artistName='Artist 1', genre=self.genre, votes=0, slug='artist-1')

    def test_vote_button_view_success(self):
        response = self.client.get(reverse('awards:vote_artist'), {'artistName': self.artist.artistName, 'genre': self.genre.slug , 'username': self.user.username})
        self.assertEqual(response.status_code, 200)
        self.artist.refresh_from_db()
        self.assertEqual(self.artist.votes, 1)
        self.vote.refresh_from_db()
        self.assertTrue(self.vote.jazzVoted)
        self.assertIn(f"Number of votes: {self.artist.votes}", response.content.decode('utf-8'))



