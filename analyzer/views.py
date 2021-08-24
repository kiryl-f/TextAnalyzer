import logging

from django.http import HttpResponse

from .forms import TextForm
from .models import Text
from django.shortcuts import render


def average_word_count(text):
    cnt = 0
    sentences = text.split('.')
    for sentence in sentences:
        cnt += sentence.count(' ') + 1
    return cnt//len(sentences)


def data(request):
    words_cnts = list()
    for text in Text.objects.all():
        words_cnts.append(average_word_count(text.text))
    res = zip(Text.objects.all(), words_cnts)
    return render(request,
                  'index.html',
                  context={'res': res})


def hello(request):
    return render(request, 'first_page.html')


def form(request):
    error = ''
    if request.method == 'POST':
        form_ = TextForm(request.POST)
        if form_.is_valid():
            title = form_.cleaned_data['title']
            text = form_.cleaned_data['text']
            av_word_cnt = average_word_count(text)
            data = {
                'title': title,
                'text': text,
                'cnt': av_word_cnt
            }
            form_.save()
            return render(request,
                          'text_data.html',
                          data)
        else:
            error = 'An error occurred'
    form_ = TextForm()
    data = {
        'form': form_
    }
    return render(request, 'form.html', data)


def delete_text(request, title):
    Text.objects.filter(title=title).delete()
    return HttpResponse('Text deleted')


def delete_all_texts(request):
    Text.objects.all().delete()
    return HttpResponse('All texts deleted')

