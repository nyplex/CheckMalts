from django.db import models

# Create your models here.

class MatchingQuestions(models.Model):
    
    answer = models.CharField(null=True, blank=False, max_length=255)
    
    def __str__(self):
        return self.answer.capitalize()


class EnjoyCheckMalt(models.Model):
    non_enjoy = models.IntegerField(null=False, blank=True, default=0)
    enjoy = models.IntegerField(null=False, blank=True, default=0)