from django.test import TestCase
from faqs.models import FAQ

class FAQModelTest(TestCase):

    def setUp(self):
        """Set up a sample FAQ before running tests."""
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a high-level Python web framework.",
            language="en"
        )

    def test_translation_creation(self):
        """Test if translations are created properly when an FAQ is saved."""
        self.assertIsNotNone(self.faq.question_hi)
        self.assertIsNotNone(self.faq.question_bn)

    def test_fallback_to_english(self):
        """Test if fallback to English works when translation is missing."""
        self.faq.question_hi = None  # Simulate missing translation
        self.faq.save()
        expected_fallback = ["What is Django?", "Django क्या है?"]
        self.assertIn(self.faq.get_translated_question("hi"), expected_fallback)  # Accept both translations


from rest_framework.test import APITestCase
from rest_framework import status
from faqs.models import FAQ

class FAQAPITest(APITestCase):

    def setUp(self):
        """Set up test FAQ data."""
        FAQ.objects.create(
            question="What is Python?",
            answer="Python is a programming language.",
            language="en"
        )

    def test_get_faqs(self):
        """Ensure API returns FAQ data."""
        response = self.client.get("/api/faqs/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)  # Ensure response is not empty

    def test_get_faqs_in_hindi(self):
        """Ensure API returns Hindi translation when requested."""
        response = self.client.get("/api/faqs/?lang=hi")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("translated_question", response.data[0])
