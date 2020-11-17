from django.db import models

# Create your models here.

class Quiz(models.Model):

    quiz_name = models.CharField(max_length=255)

    class Meta:
        verbose_name = ('Quiz')
        verbose_name_plural = ('Quiz')

    def __str__(self):
        return self.quiz_name


class QuizQuestion(models.Model):

    quiz = models.ForeignKey(Quiz, related_name='question_set_quiz', on_delete=models.CASCADE)
    question = models.TextField()

    class Meta:
        verbose_name = ('QuizQuestion')
        verbose_name_plural = ('QuizQuestion')

    def __str__(self):
        return self.question


class Options(models.Model):

    question = models.ForeignKey(QuizQuestion, related_name='option_set_question', on_delete=models.CASCADE)
    option = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    class Meta:
        verbose_name = ('Options')
        verbose_name_plural = ('Options')

    def __str__(self):
        return self.option
