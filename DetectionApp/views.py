from django.http import HttpResponse
from django.shortcuts import render
from inltk.inltk import setup
setup('hi')
from inltk.inltk import get_sentence_similarity

# Create your views here.
def index(request):
    if request.method == "GET":
        return render(request, 'index.html')
    else:
        phrase1 = request.POST["phrase1"];
        phrase2 = request.POST["phrase2"];
        similarlity = get_sentence_similarity(phrase1, phrase2, 'hi')
        return HttpResponse(similarlity);