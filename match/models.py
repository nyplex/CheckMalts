from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class MatchingQuestions(models.Model):
    
    answer = models.CharField(null=True, blank=False, max_length=255)
    
    def __str__(self):
        return self.answer.capitalize()
    