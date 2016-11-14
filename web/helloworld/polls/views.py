# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

import json

def index(request):
    #return HttpResponse(request,"polls/templates/hello.html",{})
    return render(request,"polls/hello.html",{})
#    List = ['自强学堂', '渲染Json到模板']
#    Dict = {'site': '自强学堂', 'author': '涂伟忠'}
#    return render(request, 'hello.html', {
#            'List': json.dumps(List),
#            'Dict': json.dumps(Dict)
#        })
