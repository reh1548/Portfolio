from django.test import TestCase
from django.urls import reverse
from .models import Projects

# Create your tests here.
# base/tests.py


class ProjectsModelTests(TestCase):

    def setUp(self):
        self.project = Projects.objects.create(
            project_name='Test Project',
            project_image_link='http://example.com/image.jpg',
            project_link='http://example.com/project'
        )

    def test_project_creation(self):
        self.assertEqual(self.project.project_name, 'Test Project')
        self.assertEqual(self.project.project_image_link, 'http://example.com/image.jpg')
        self.assertEqual(self.project.project_link, 'http://example.com/project')
        self.assertEqual(str(self.project), 'Project: Test Project \n\nhttp://example.com/project')

class ViewsTests(TestCase):

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/index.html')

    def test_about_view(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/about.html')

    def test_contact_view_get(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/contact.html')

    def test_contact_view_post(self):
        response = self.client.post(reverse('contact'), {
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'This is a test message.'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/contact.html')

    def test_projects_view(self):
        Projects.objects.create(
            project_name='Test Project',
            project_image_link='http://example.com/image.jpg',
            project_link='http://example.com/project'
        )
        response = self.client.get(reverse('projects'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/projects.html')
        self.assertContains(response, 'Test Project')
