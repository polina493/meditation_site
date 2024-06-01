from django.test import TestCase
from django.contrib.auth import get_user_model
from core.models import Note
from django.urls import reverse

User = get_user_model()

class ModelTestCase(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(username="testuser", password="securepassword")
        self.assertEqual(user.username, "testuser")

    def test_note_creation(self):
        user = User.objects.create_user(username="testuser", password="securepassword")
        note = Note.objects.create(user=user, title="Test Note", content="Test content")
        self.assertEqual(note.user.username, "testuser")

class UserAccountTests(TestCase):
    def test_signup_page_url(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/signup.html') 

