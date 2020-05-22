from django.db import models

# Create your models here.

<<<<<<< HEAD
class Rate(models.Model):
    grade = models.models.IntegerField()
=======

class Menber(models.Model):
    name = models.models.CharField(max_length=50)
>>>>>>> 33de6f63026ca2292dd096bd39dea55b6ed51f3b

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text



