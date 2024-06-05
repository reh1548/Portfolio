from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Blog, BlogImage, Comment
from tinymce.models import HTMLField
from datetime import date

# Create your tests here.
# blog/tests.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Blog, BlogImage, Comment
from tinymce.models import HTMLField
from datetime import date

class BlogModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.blog_image = BlogImage.objects.create(image='blog_images/test_image.jpg')
        self.blog = Blog.objects.create(
            author=self.user,
            title='Test Blog',
            subtitle='Test Subtitle',
            main_image='blog_images/main_image.jpg',
            content='This is a test blog content'
        )
        self.blog.additional_images.add(self.blog_image)

    def test_blog_creation(self):
        self.assertEqual(self.blog.title, 'Test Blog')
        self.assertEqual(self.blog.subtitle, 'Test Subtitle')
        self.assertEqual(self.blog.author, self.user)
        self.assertEqual(self.blog.main_image, 'blog_images/main_image.jpg')
        self.assertEqual(str(self.blog), 'Test Blog')
        self.assertIn(self.blog_image, self.blog.additional_images.all())

    # def test_blog_image_creation(self):
    #     self.assertEqual(self.blog_image.image, 'blog_images/test_image.jpg')
    #     self.assertEqual(str(self.blog_image), 'Image 1')

class CommentModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.blog = Blog.objects.create(
            author=self.user,
            title='Test Blog',
            subtitle='Test Subtitle',
            main_image='blog_images/main_image.jpg',
            content='This is a test blog content'
        )
        self.comment = Comment.objects.create(
            user=self.user,
            blog=self.blog,
            comment='This is a test comment'
        )

    def test_comment_creation(self):
        self.assertEqual(self.comment.user, self.user)
        self.assertEqual(self.comment.blog, self.blog)
        self.assertEqual(self.comment.comment, 'This is a test comment')
        self.assertEqual(str(self.comment), f'Comment by {self.user.username} on {self.blog.title}')

class ViewsTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.blog = Blog.objects.create(
            author=self.user,
            title='Test Blog',
            subtitle='Test Subtitle',
            main_image='blog_images/main_image.jpg',
            content='This is a test blog content'
        )

    def test_blog_view(self):
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog.html')
        self.assertContains(response, 'Test Blog')

    def test_blog_single_view(self):
        response = self.client.get(reverse('blog_single', args=[self.blog.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_single.html')
        self.assertContains(response, 'Test Blog')

    def test_add_comment_view_post(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('add_comment', args=[self.blog.id]), {
            'comment': 'This is a test comment'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect to blog_single
        self.assertTrue(Comment.objects.filter(blog=self.blog, comment='This is a test comment').exists())

    def test_add_comment_view_post_not_logged_in(self):
        response = self.client.post(reverse('add_comment', args=[self.blog.id]), {
            'comment': 'This is a test comment'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect to login
        self.assertFalse(Comment.objects.filter(blog=self.blog, comment='This is a test comment').exists())

    def test_add_comment_view_post_empty_comment(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('add_comment', args=[self.blog.id]), {
            'comment': ''
        })
        self.assertEqual(response.status_code, 302)  # Should redirect to blog_single
        self.assertFalse(Comment.objects.filter(blog=self.blog, comment='').exists())

