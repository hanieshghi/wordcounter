from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request , 'home.html')

def count(request):
    words = request.GET['fulltext']
    wordslist = words.split()
    wordscounter = {}
    
    for word in wordslist:
        wordscounter[word] = wordscounter.get(word,0)+1

    return render(request , 
        'count.html', {'yourtext': words , 
        'wordnums':len(wordslist), 'wordcounters':wordscounter.items() })

def about(request):
    return render(request, 'about.html')