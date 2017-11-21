# coding:utf-8

from django.db import models


class EsAddress(models.Model):
    """
    es地理位置
    """
    address = models.CharField(max_length=64)
    is_used = models.BooleanField(default=False)

    def __unicode__(self):
        return self.address

    class Meta:
        db_table = 'es_address'

