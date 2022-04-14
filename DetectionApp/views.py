from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    if request.method == "GET":
        return render(request, 'index.html')

    elif request.method == "POST":
        from inltk.inltk import setup
        setup('hi')
        print("YESS 1")
        # from inltk.inltk import get_sentence_similarity
        print("YESS 2")

        phrase1 = "भेजना चाहते हैं हिंदी में मैसेज लेकिन नहीं आती टाइपिंग |"
        phrase2 = "भेजना चाहते हैं हिंदी में मैसेज लेकिन नहीं आती टाइपिंग |"
        # similarlity = get_sentence_similarity(phrase1, phrase2, 'hi')
        from inltk.inltk import get_similar_sentences
        get_similar_sentences(phrase1, 1, 'hi', degree_of_aug = 0.1)

        print("YESS 3")

        # return HttpResponse(similarlity);