# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the recuento index. In a near future this will be the entry point to the rest API")
