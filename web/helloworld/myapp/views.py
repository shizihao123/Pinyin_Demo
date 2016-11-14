# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def hello(request):
	return render(request, "myapp/templates/hello.html",{})
# Create your views here.
