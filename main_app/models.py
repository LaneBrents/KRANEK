from django.db import models
from django.db import reverse
from django.contrib.auth.models import User

#================================================================================================#

        # Create our models here

# class Flashcard(models.Model):

# class Card(models.Model):

# class Quiz(models.Model):

# class Questions(models.Model):

# class Photo(models.Model):
#     url = models.CharField(max_length=200)
#     flashcard = models.ForeignKey(Card, on_delete=models.CASCADE)
#     quiz = models.ForeignKey(Question, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"photo for card_id: {self.flashcard_id} @{self.url}"
#         return f"photo for question_id: {self.flashcard_id} @{self.url}"

class Quiz(models.Model):
  title = models.CharField(max_length=100)
  question = models.CharField(max_length=250)
  answer = models.TextField(max_length=250)
  pofile = models.ForeignKey(Profile, on_delete=models.CASCADE)


