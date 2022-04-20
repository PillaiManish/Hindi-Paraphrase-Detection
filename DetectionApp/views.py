from django.http import HttpResponse
from django.shortcuts import render
from inltk.inltk import setup
setup('hi')
from inltk.inltk import get_sentence_similarity

# Create your views here.
def index(request):
    if request.method == "GET":
        session = {}
        session['display'] = False
        session['value'] = 0
        return render(request, 'index.html', session)

    elif request.method == "POST":
        phrase1 = request.POST["phrase1"];
        phrase2 = request.POST["phrase2"];
        similarlity = get_sentence_similarity(phrase1, phrase2, 'hi')

        session = {}
        session['display'] = True
        session['value'] = similarlity
        return render(request, 'index.html', session);
