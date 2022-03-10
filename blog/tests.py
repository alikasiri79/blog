from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from django.shortcuts import reverse


# Create your tests here.


class BlogPostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='user1')
        cls.post = Post.objects.create(
            title='Post1',
            text='hi',
            author=cls.user,
            status=Post.STATUS_CHOICES[0][0]

        )
        cls.post2 = Post.objects.create(
            title='Post2',
            text='hi2',
            author=cls.user,
            status=Post.STATUS_CHOICES[1][0]

        )

    def test_url_home_page(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)

    def test_url_home(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_not_found_page(self):
        response = self.client.get('/blog/1000/')
        self.assertEqual(response.status_code, 404)

    def test_draft_post(self):
        response = self.client.get(reverse('post_list'))
        self.assertNotContains(response, self.post2.title)

    def test_url_post(self):
        response = self.client.get(reverse('post_detail', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)

    def test_post_create_view(self):
        response = self.client.post(reverse('post_create'), {
            'title': 'post test',
            'text': 'post test',
            'status': 'pub',
            'author': self.user.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title,'post test')

    def test_post_update_view(self):
        response = self.client.post(reverse('post_update', args=[self.post.id]), {
            'title': 'post update',
            'text': 'post update text',
            'status': 'pub',
            'author': self.user.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.first().title,'post update')

    def test_post_delete_view(self):
        response = self.client.post(reverse('post_delete', args=[self.post.id]))
        self.assertEqual(response.status_code, 302)
