from django.shortcuts import render
from .models import Question

def quiz(request):
    questions = Question.objects.all()
    return render(request, 'quiz/quiz.html', {'questions': questions})
