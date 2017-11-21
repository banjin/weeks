# coding:utf-8

from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
# Create your views here.
from django.conf import settings
from week1_1105.models import EsAddress


def get_es_url(request):
    """
    获取es
    :param request:
    :return:
    """

    print "xxxxx {}".format(settings.ES_URL)
    return HttpResponse('{}'.format(settings.ES_URL))


def update_es_address(request):
    """
    修改es状态
    :param request:True
    :return:
    """
    EsAddress.objects.filter(pk=1).update(is_used=True)
    st = EsAddress.objects.filter(pk=1).values_list('is_used')[0]
    return JsonResponse({"status": 200, 'st': st})
