from django.shortcuts import render
from django.http import Http404
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from qa.models import Question, Answer

# Create your views here.
from django.http import HttpResponse

def test(request, *args, **kwargs):
    return HttpResponse('OK', status=200)

def all(request):
    return show(request,Questions.objects.new())

def popular(request):
    return show(request,Questions.objects.popular())


# new questions view
def show(request,query):
    limit = 10 # hadrcoding!!!
    page = request.GET.get('page', 1) #hardcoding !!!
    paginator = Paginator(query, limit)
    paginator.baseurl = reverse('urls:id')
    page = paginator.page(page) # Page
    return render(request, 'all.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
})

def question(request, id):
    try:
        question = Question.objects.get(pk=id)
    except Question.DoesNotExist:
        raise Http404
    answers=Answer.get_by_id(id)
    return render(request, 'question.html', {
        'question': question,
        'answers': answers
    })