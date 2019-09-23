from django.db import models
from datetime import *
from django.contrib.auth.models import User


class webserver(models.Model):
    user = models.OneToOneField(User, unique=True, verbose_name=("用户"))
    phone = models.CharField("手机", max_length=20)
    user_role = models.CharField('角色', max_length=40)


class cabinet(models.Model):
    name = models.CharField('名称', max_length=30)
    power = models.CharField('权限', max_length=20)

    class Meta:
        db_table = "cabinet"


class hostinfo(models.Model):
    hostname = models.CharField('主机名', max_length=255)
    IP = models.CharField('IP地址', max_length=50)
    Mem = models.IntegerField('内存')
    CPU = models.CharField('cpu', max_length=255)
    CPUS = models.IntegerField('cpus')
    OS = models.CharField('os', max_length=255)
    kernelrelease = models.CharField('kernelrelease', max_length=255)
    virtual1 = models.CharField('virtual', max_length=255)
    biosversion = models.CharField('biosversion', max_length=255)
    serialnumber = models.CharField('serialnumber', max_length=255)
    status = models.CharField('状态', max_length=50)

    def __str__(self):
        return self.hostname


class product(models.Model):
    service_name = models.CharField('服务名称', max_length=20)
    pid = models.IntegerField('pid')
    module_letter = models.CharField(max_length=10)

    class Meta:
        db_table = "product"


class monitorMemory(models.Model):
    hostid = models.IntegerField('监控主机ID')
    avai = models.CharField('空闲内存', max_length=20)
    total = models.CharField('总内存', max_length=20)
    ratio = models.CharField('使用率', max_length=20)
    time = models.DateTimeField('时间', auto_now_add=True)
