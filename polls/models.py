from django.db import models

# Create your models here.

# Модель для обработки вопроса
class Question(models.Model):
    text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    # В момент конвертации в str() 
    def __str__(self):
        return self.text


# Модель для обработки варианта ответа на вопрос
class Choice(models.Model):
    # Связываем Quetions и Choices
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    votes = models.IntegerField(default=0)
    # В момент конвертации в str() 
    def __str__(self):
        return self.text
