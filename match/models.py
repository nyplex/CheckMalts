from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class MatchingQuestions(models.Model):
    
    CHOICES = [('1', 'dry'), ('2', 'sweet'), ('3', 'party hard'),
               ('4', 'party calm'), ('5', 'romantic date'), ('6', 'after work'),
               ('7', 'party'), ('8', 'single'), ('9', 'double'), ('10', 'vodka'),
               ('11', 'rum'), ('12', 'tequilla'), ('13', 'old school'), ('14', 'contempory')]
    
    answer = models.CharField(null=True, blank=False, max_length=255, choices=CHOICES)
    
    def __str__(self):
        print(self.answer)
        return self.get_answer_display().capitalize()
        #return self.answer.capitalize()
    