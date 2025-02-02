from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    LANGUAGE_CHOICES = [
        ('en', 'English'),
        ('hi', 'Hindi'),
        ('bn', 'Bengali'),
    ]

    question = models.TextField()
    answer = RichTextField()
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default='en')

    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        """Automatically translate the question into Hindi and Bengali before saving."""
        translator = Translator()

        if not self.question_hi:
            try:
                self.question_hi = translator.translate(self.question, src='en', dest='hi').text
            except Exception:
                self.question_hi = self.question  # Fallback to English

        if not self.question_bn:
            try:
                self.question_bn = translator.translate(self.question, src='en', dest='bn').text
            except Exception:
                self.question_bn = self.question  # Fallback to English

        super().save(*args, **kwargs)

    def get_translated_question(self, lang='en'):
        """Return the question in the requested language with fallback to English."""
        if lang == 'hi' and self.question_hi:
            return self.question_hi
        elif lang == 'bn' and self.question_bn:
            return self.question_bn
        return self.question  # Default fallback to English

    def __str__(self):
        return self.question

