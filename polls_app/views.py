from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from .models import Question, Choice


def index(req):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    return render(req, 'polls/polls_index.html', {'latest_question_list': latest_question_list})


def detail(req, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    return render(req, 'polls/detail.html', {'question': question})


def results(req, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    return render(req, 'polls/results.html', {'question': question})
    pass


def vote(req, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    try:
        selected_choice = question.choice_set.get(pk=req.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {
            'question': question,
            'error_message': "You didn`t select a choice"
        }
        return render(req, 'polls/detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save(update_fields=['votes'])
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
