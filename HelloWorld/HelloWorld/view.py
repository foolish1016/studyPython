# -*- coding: UTF-8 -*-
from django.http import HttpResponse
def index(request):
    return HttpResponse(u"千里之行，始于足下！")