# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
sys.path.append("/home/jun/workspace/Pinyin_Demo")
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from pinyinSplit.pinyinSplit import *

def find_hanzi(input):
        tokenizer = PinyinTokenizer()
        # # print tokenizer.tokenize('woaibeijingtiananmentiananmenshangtaiyangsheng')
        # print tokenizer.tokenize(input)
        pinyin_list = tokenizer.tokenize(input)
        print pinyin_list
        V = viterbi(pinyin_list)

        i = 0
        for phrase, prob in sorted(V.items(), key=lambda d: d[1], reverse=True):
            return  phrase
            break
        #    i += 1
        #    if i >= 5:
        #        break


def add(request):
    a = request.POST['a']
    c = find_hanzi(a)
    print "hello " + c 
    return HttpResponse((u' '+ c).encode('utf-8').strip())
    #return HttpResponse(u"你好".encode('utf-8').strip())

def show(request):
    return render(request, 'base.html')

