from django.db import models
from django.utils import timezone
import datetime

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    publication_date = models.DateTimeField("Datefield")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.publication_date >= timezone.now() - datetime.timedelta(days=1)


class Choices(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    def __str__(self):
        return self.choice_text
