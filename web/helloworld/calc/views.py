# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
sys.path.append("/home/jun/workspace/Pinyin_Demo")
from django.shortcuts import render

# Create your views here.
from web.helloworld.calc import *
from django.shortcuts import render
from django.http import HttpResponse
from pinyinSplit.pinyinSplit import *
import json
from django.http import JsonResponse


def find_hanzi(input):
    tokenizer = PinyinTokenizer()
    pinyin_list = tokenizer.tokenize(input)
    print pinyin_list
    # start_mat, transition_mat, emission_mat, pinyin_mat = prepare_mat()
    # V = viterbi(pinyin_list)
    V = viterbi(pinyin_list, start_mat, transition_mat, emission_mat, pinyin_mat)
    result = {}
    if V == {}:
        return ""
    i = 0
    for phrase, prob in sorted(V.items(), key=lambda d: d[1], reverse=True):
        if i >= 10:
            break
        result[i] = phrase
        print phrase
        i += 1
    return result


def add(request):
    pinyin = request.POST.get('pinyin',"n")
    num = request.POST.get('num', '-1')
    if num == '-1':
        return show(request)
    result = find_hanzi(pinyin)
    # print "request  number: ",  num
    hanzi_json = json.JSONEncoder().encode(result)
    print hanzi_json
    # name_dict = {'num':num.encode('utf-8').strip(), 'hanzi':{result}(u' '+ hanzi).encode('utf-8').strip()}
    name_dict = {'num':num.encode('utf-8').strip(), 'hanzi':hanzi_json}
    return JsonResponse(name_dict)
    # return HttpResponse((u' '+ c).encode('utf-8').strip())
    # return HttpResponse(u"你好".encode('utf-8').strip())


def show(request):
    return render(request, 'base.html')

