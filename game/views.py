from django.http import HttpResponse
from django.shortcuts import render
from .models import Word
import random
import arabic_reshaper


def guess_word(request):
    if request.method == 'GET':
        word_list = list(Word.objects.values_list('name', flat=True))
        word = random.choice(word_list)
        word_reshape = arabic_reshaper.reshape(word)
        harf = random.choice(word_reshape)
        index_harf = word_reshape.index(harf)
        harf_send = word[index_harf]
        data_send = word_reshape.replace(harf, '_', 1)

        context = {'data': data_send,'harf_send': harf_send}
        return render(request, 'game/main.html', context)

    if request.method == 'POST':
        harf_receive = request.POST.get('harf_receive')
        harf_send = request.POST.get('harf_send')


        if harf_receive == harf_send:
            answer = 'آفرین، پاسخ شما درست بود.'
        else:
            if harf_receive != '_':
                answer = 'نه نشد، دوباره امتحان کن.'

        contex = {'answer': answer}
        return render(request, 'game/result.html', contex)