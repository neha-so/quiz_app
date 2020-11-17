from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Quiz, QuizQuestion

# Create your views here.


class QuizListView(ListView):
    """Quiz list view."""

    template_name = 'home.html'
    model = Quiz
   
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(QuizListView, self).dispatch(*args, **kwargs)


class QuestionListView(ListView):
	"""Show list of questions for selected quiz."""

	template_name = "question-list.html"
	model = QuizQuestion

	def get_queryset(self):
		return self.model.objects.filter(quiz__id=self.kwargs['pk'])
