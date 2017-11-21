# coding:utf-8

from week1_1105.models import EsAddress
from django.conf import settings


class GetEsConfig(object):
    """
    动态修改es配置.
    """

    def process_request(self, request):
        try:
            es_address = EsAddress.objects.get(is_used=True)
            print "!!!!!!!!"
        except EsAddress.DoesNotExist:
            settings.ES_URL = "this is null"
            print "DDDDD"
        else:
            print ".............."
            print "ES_URL...", settings.ES_URL
            settings.ES_URL = es_address.address
        return None


