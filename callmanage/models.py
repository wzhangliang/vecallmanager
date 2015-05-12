# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Autologin(models.Model):
    extno = models.CharField(max_length=10)
    userno = models.CharField(max_length=10)
    sx = models.CharField(max_length=4, blank=True)

    class Meta:
        managed = False
        db_table = 'autologin'


class BusinessTransferplan(models.Model):
    groupid = models.CharField(max_length=10, blank=True)
    starttime = models.CharField(max_length=20, blank=True)
    endtime = models.CharField(max_length=20, blank=True)
    tansfertype = models.CharField(max_length=1, blank=True)
    transferwhere = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 'business_transferplan'


class Businessgroup(models.Model):
    groupid = models.CharField(max_length=4, blank=True)
    groupname = models.CharField(max_length=20, blank=True)
    callno = models.TextField(blank=True)
    vocname = models.TextField(blank=True)
    useivr = models.CharField(max_length=1, blank=True)
    directto = models.CharField(max_length=20, blank=True)
    filepath = models.CharField(max_length=200, blank=True)
    vocprompt = models.CharField(max_length=20, blank=True)
    sourcetype = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'businessgroup'


class CallCallevaluate(models.Model):
    evaluateid = models.CharField(max_length=2)
    evaluatename = models.CharField(max_length=30)
    bzbz = models.CharField(max_length=200, blank=True)

    class Meta:
        managed = False
        db_table = 'call_callevaluate'


class CallCalloutlineinfo(models.Model):
    lines = models.CharField(max_length=50, blank=True)
    calloutno = models.CharField(max_length=50, blank=True)
    callnos = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'call_calloutlineinfo'


class CallCallpara(models.Model):
    callparaid = models.CharField(max_length=4)
    callparavalue = models.CharField(max_length=120, blank=True)
    callparamemo = models.CharField(max_length=200, blank=True)

    class Meta:
        managed = False
        db_table = 'call_callpara'


class CallCallrecord(models.Model):
    callfromdatetime = models.CharField(max_length=20)
    callenddatetime = models.CharField(max_length=20)
    calldurationtime = models.CharField(max_length=12)
    calltype = models.CharField(max_length=2, blank=True)
    callno = models.CharField(max_length=60)
    calltrunckno = models.CharField(max_length=12)
    calluerno = models.CharField(max_length=12, blank=True)
    calldtmfno = models.CharField(max_length=60)
    customername = models.CharField(max_length=60, blank=True)
    username = models.CharField(max_length=30, blank=True)
    callrecordid = models.CharField(max_length=60)
    ucdchanno = models.IntegerField(blank=True, null=True)
    ucdgroupid = models.CharField(max_length=4, blank=True)
    trundatetime = models.CharField(max_length=20, blank=True)
    hangupdatetime = models.CharField(max_length=20, blank=True)
    gjlx = models.CharField(max_length=1, blank=True)
    zjf = models.CharField(max_length=1, blank=True)
    recordfilename = models.CharField(max_length=200, blank=True)
    seledatetime = models.CharField(max_length=20, blank=True)
    recordtype = models.CharField(max_length=2, blank=True)
    recordyhbh = models.CharField(max_length=30, blank=True)
    callevaluate = models.CharField(max_length=1, blank=True)
    smuser = models.TextField(blank=True)
    sendmessagetime = models.CharField(max_length=20, blank=True)
    ifplayed = models.CharField(max_length=1, blank=True)
    ringtime = models.CharField(max_length=50, blank=True)
    talktime = models.CharField(max_length=50, blank=True)
    cpstaskid = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 'call_callrecord'


class CallChan(models.Model):
    channo = models.IntegerField()
    chantype = models.IntegerField()
    chandialno = models.CharField(max_length=20)
    useivr = models.CharField(max_length=1, blank=True)
    directto = models.CharField(max_length=20, blank=True)
    recordflag = models.CharField(max_length=1, blank=True)
    smssendtoip = models.CharField(max_length=30, blank=True)
    smssendtoport = models.CharField(max_length=4, blank=True)
    chanstatus = models.CharField(max_length=60, blank=True)
    chancallid = models.CharField(max_length=60, blank=True)
    chancallname = models.CharField(max_length=200, blank=True)
    chandtmf = models.CharField(max_length=60, blank=True)
    chancalldatetime = models.CharField(max_length=20, blank=True)
    chanendcalldatetime = models.CharField(max_length=20, blank=True)
    chandualtime = models.CharField(max_length=18, blank=True)
    onlineflag = models.CharField(max_length=2, blank=True)
    chanucdgroup = models.CharField(max_length=1, blank=True)
    currentuser = models.CharField(max_length=30, blank=True)
    chanlinkchan = models.IntegerField(blank=True, null=True)
    linestatus = models.IntegerField(blank=True, null=True)
    recordfileid = models.CharField(max_length=32, blank=True)
    inout = models.CharField(max_length=1, blank=True)
    binip = models.CharField(max_length=20, blank=True)
    binport = models.CharField(max_length=5, blank=True)
    ucdgroupid = models.CharField(max_length=4, blank=True)
    trundatetime = models.CharField(max_length=20, blank=True)
    hangupdatetime = models.CharField(max_length=20, blank=True)
    card = models.IntegerField(blank=True, null=True)
    hxtdjj = models.CharField(max_length=10, blank=True)
    hxtchanno = models.IntegerField(blank=True, null=True)
    linename = models.CharField(max_length=20, blank=True)
    outdialno = models.CharField(max_length=20, blank=True)
    tollno = models.CharField(max_length=20, blank=True)
    mainline = models.IntegerField(blank=True, null=True)
    ifmain = models.IntegerField(blank=True, null=True)
    pickupno = models.CharField(max_length=20, blank=True)
    mailline = models.IntegerField(blank=True, null=True)
    voicename = models.CharField(max_length=20, blank=True)
    dtmf = models.CharField(max_length=1, blank=True)
    mainno = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 'call_chan'


class CallChandj(models.Model):
    dspmodno = models.IntegerField()
    channo = models.IntegerField()
    chandialno = models.CharField(max_length=20, blank=True)
    onlineflag = models.CharField(max_length=20, blank=True)
    currentuser = models.CharField(max_length=30, blank=True)
    useanalog = models.CharField(max_length=1, blank=True)
    directto = models.CharField(max_length=20, blank=True)
    catno = models.CharField(max_length=1, blank=True)
    bgh = models.CharField(max_length=50, blank=True)
    recordflag = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'call_chandj'


class CallChanrecordings(models.Model):
    tapichanno = models.CharField(max_length=20)
    channelhandle = models.DecimalField(db_column='channelHandle', max_digits=10, decimal_places=0)  # Field name made lowercase.
    dev = models.IntegerField()
    pcm = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'call_chanrecordings'


class CallEnablecall(models.Model):
    lx = models.CharField(max_length=1)
    bh = models.CharField(max_length=10)
    n_all = models.CharField(max_length=1)
    n_gn = models.CharField(max_length=1)
    n_gj = models.CharField(max_length=1)
    n_tel = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'call_enablecall'


class CallHmd(models.Model):
    tel = models.CharField(max_length=30)
    bussinessgroupid = models.CharField(max_length=4, blank=True)

    class Meta:
        managed = False
        db_table = 'call_hmd'



class CallIp(models.Model):
    iplist = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'call_ip'


class CallIvr(models.Model):
    ivrindex = models.CharField(max_length=20)
    ivrname = models.CharField(max_length=20)
    channelno = models.CharField(max_length=100, blank=True)
    noticepath = models.CharField(max_length=100, blank=True)
    operatetype = models.CharField(max_length=50, blank=True)
    content = models.CharField(max_length=50, blank=True)
    operatekey = models.CharField(max_length=50, blank=True)

    class Meta:
        managed = False
        db_table = 'call_ivr'


class CallIvroperatetype(models.Model):
    operatetype = models.IntegerField()
    operatevalue = models.CharField(max_length=50, blank=True)

    class Meta:
        managed = False
        db_table = 'call_ivroperatetype'


class CallLimitgroup(models.Model):
    limitgroupid = models.CharField(max_length=4)
    limitgroupname = models.CharField(max_length=30)
    limitgroupdialno = models.CharField(max_length=200, blank=True)
    limitgroupmemo = models.CharField(max_length=200, blank=True)

    class Meta:
        managed = False
        db_table = 'call_limitgroup'


class CallLimitgroupuser(models.Model):
    limitgroupid = models.CharField(max_length=4)
    channo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'call_limitgroupuser'


class CallOnlineflag(models.Model):
    bh = models.CharField(max_length=2)
    mc = models.CharField(max_length=10, blank=True)
    jtdj = models.CharField(max_length=4, blank=True)
    sfjt = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'call_onlineflag'


class CallPickupgroup(models.Model):
    pickupgroupid = models.CharField(max_length=4)
    pickupgroupname = models.CharField(max_length=30)
    pickupgroupmemo = models.CharField(max_length=200, blank=True)

    class Meta:
        managed = False
        db_table = 'call_pickupgroup'


class CallPickupgroupuser(models.Model):
    pickupgroupid = models.CharField(max_length=4)
    orderid = models.IntegerField()
    ucdgroupid = models.CharField(max_length=4, blank=True)
    type = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'call_pickupgroupuser'





class CallRecordings(models.Model):
    callfromdatetime = models.CharField(max_length=20)
    callenddatetime = models.CharField(max_length=20)
    calldurationtime = models.CharField(max_length=12)
    inout = models.CharField(max_length=1)
    callno = models.CharField(max_length=60)
    calltrunckno = models.CharField(max_length=12)
    calluerno = models.CharField(max_length=8)
    calldtmfno = models.CharField(max_length=60, blank=True)
    callrecordid = models.CharField(max_length=32, blank=True)
    ucdchanno = models.CharField(max_length=20, blank=True)
    hangupdatetime = models.CharField(max_length=20, blank=True)
    recordfilename = models.CharField(max_length=200, blank=True)
    filesize = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'call_recordings'


class CallRecordtype(models.Model):
    recordtype = models.CharField(max_length=2)
    recordname = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'call_recordtype'


class CallStatus(models.Model):
    linestatus = models.IntegerField()
    chinesestatus = models.CharField(max_length=30, blank=True)
    bzbz = models.CharField(max_length=200, blank=True)

    class Meta:
        managed = False
        db_table = 'call_status'


class CallStatus2(models.Model):
    linestatus = models.IntegerField(primary_key=True)
    chinesestatus = models.CharField(max_length=30, blank=True)
    bzbz = models.CharField(max_length=200, blank=True)

    class Meta:
        managed = False
        db_table = 'call_status2'


class CallSubcallrecord(models.Model):
    callfromdatetime = models.CharField(max_length=20)
    callenddatetime = models.CharField(max_length=20)
    calldurationtime = models.CharField(max_length=12)
    calltype = models.CharField(max_length=1)
    zjsxh = models.CharField(max_length=1)
    calluerno = models.CharField(max_length=8)
    calldtmfno = models.CharField(max_length=60)
    username = models.CharField(max_length=30, blank=True)
    callrecordid = models.CharField(max_length=32)
    hangupdatetime = models.CharField(max_length=20, blank=True)
    gjlx = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'call_subcallrecord'


class CallUcdrecord(models.Model):
    id = models.IntegerField(primary_key=True)
    channo = models.IntegerField(blank=True, null=True)
    chantype = models.IntegerField(blank=True, null=True)
    yhbh = models.CharField(max_length=8, blank=True)
    fjh = models.CharField(max_length=8, blank=True)
    flag = models.CharField(max_length=3, blank=True)
    begindatetime = models.CharField(max_length=20, blank=True)
    enddatetime = models.CharField(max_length=20, blank=True)
    durationtime = models.IntegerField(blank=True, null=True)
    ucdgroupid = models.CharField(max_length=4, blank=True)
    export_zt = models.CharField(max_length=1, blank=True)
    chandialno = models.CharField(max_length=20, blank=True)
    callevalue = models.CharField(max_length=2, blank=True)
    compid = models.CharField(max_length=20, blank=True)
    callindatetime = models.CharField(max_length=20, blank=True)
    callno = models.CharField(max_length=50, blank=True)

    class Meta:
        managed = False
        db_table = 'call_ucdrecord'


class CallUcdrecordSendcfg(models.Model):
    id = models.IntegerField(primary_key=True)
    sfkq = models.CharField(max_length=1)
    url = models.TextField()
    createtime = models.CharField(max_length=20)
    compid = models.CharField(max_length=20, blank=True)
    by1 = models.CharField(max_length=20, blank=True)
    by2 = models.CharField(max_length=50, blank=True)
    by3 = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'call_ucdrecord_sendcfg'


class CallUcdrecordSendlog(models.Model):
    uuid = models.CharField(max_length=100)
    startid = models.IntegerField(blank=True, null=True)
    endid = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=1)
    nr = models.CharField(max_length=200)
    createtime = models.CharField(max_length=20)
    compid = models.CharField(max_length=20, blank=True)
    by1 = models.CharField(max_length=20, blank=True)
    by2 = models.CharField(max_length=50, blank=True)
    by3 = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'call_ucdrecord_sendlog'


class CallVip(models.Model):
    tel = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'call_vip'


class CallWxrecord(models.Model):
    callfromdatetime = models.CharField(max_length=20, blank=True)
    fjh = models.CharField(max_length=20, blank=True)
    zxh = models.CharField(max_length=20, blank=True)
    recordfilename = models.TextField(blank=True)
    recordfilepath = models.TextField(blank=True)
    msgid = models.CharField(max_length=100, blank=True)
    compwxid = models.CharField(max_length=50, blank=True)
    compid = models.CharField(max_length=50, blank=True)
    openid = models.CharField(max_length=50, blank=True)
    msgtype = models.CharField(max_length=50, blank=True)
    voicestatus = models.CharField(max_length=50, blank=True)

    class Meta:
        managed = False
        db_table = 'call_wxrecord'


class CallYshmd(models.Model):
    callno = models.CharField(max_length=10)
    ucdgroupid = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'call_yshmd'


class Calloutgroupline(models.Model):
    groupid = models.CharField(max_length=4)
    callno = models.CharField(max_length=50)
    sx = models.CharField(max_length=4, blank=True)

    class Meta:
        managed = False
        db_table = 'calloutgroupline'


class Callprocess(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=4)
    name = models.CharField(max_length=20, blank=True)
    callno = models.TextField(blank=True)
    vocname = models.CharField(max_length=20, blank=True)
    useivr = models.CharField(max_length=1, blank=True)
    directtype = models.CharField(max_length=1, blank=True)
    directto = models.CharField(max_length=20, blank=True)
    sourcetype = models.CharField(max_length=1, blank=True)
    enterno = models.CharField(max_length=2, blank=True)
    truncateplan = models.CharField(max_length=10, blank=True)
    parentcode = models.CharField(max_length=4, blank=True)
    type = models.CharField(max_length=1, blank=True)
    memo = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'callprocess'


class Company(models.Model):
    con_no = models.CharField(max_length=20)
    content = models.CharField(max_length=200, blank=True)
    remark = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 'company'


class ConfRecord(models.Model):
    id = models.IntegerField(primary_key=True)
    confname = models.CharField(max_length=200, blank=True)
    wstarttime = models.CharField(max_length=20, blank=True)
    wdurationtime = models.CharField(max_length=20, blank=True)
    rstarttime = models.CharField(max_length=20, blank=True)
    rendtime = models.CharField(max_length=20, blank=True)
    runitofstartunit = models.CharField(max_length=2, blank=True)
    rtimeofstart = models.CharField(max_length=20, blank=True)
    rtimeoffinish = models.CharField(max_length=20, blank=True)
    trunkno = models.CharField(max_length=200, blank=True)
    recordfilename = models.CharField(max_length=200, blank=True)
    remark = models.TextField(blank=True)
    rdurationtime = models.CharField(max_length=50, blank=True)
    flag = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'conf_record'


class Config(models.Model):
    paraid = models.CharField(max_length=100, blank=True)
    paravalue = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'config'


class ConfmemberRecord(models.Model):
    confid = models.IntegerField()
    callno = models.CharField(max_length=20, blank=True)
    calltype = models.CharField(max_length=20, blank=True)
    membertype = models.CharField(max_length=20, blank=True)
    membername = models.CharField(max_length=20, blank=True)
    jointime = models.CharField(max_length=20, blank=True)
    quittime = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 'confmember_record'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Dual(models.Model):
    one = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'dual'


class ExportRecord(models.Model):
    guid = models.CharField(max_length=50, blank=True)
    startid = models.IntegerField(blank=True, null=True)
    endid = models.IntegerField(blank=True, null=True)
    flag = models.CharField(max_length=2, blank=True)
    starttime = models.CharField(max_length=20, blank=True)
    endtime = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 'export_record'


class Operaterecord(models.Model):
    userid = models.CharField(max_length=20)
    operdatetime = models.CharField(max_length=20)
    opertype = models.CharField(max_length=100, blank=True)
    opersql = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'operaterecord'


class Transferplan(models.Model):
    planid = models.IntegerField()
    recordtype = models.CharField(max_length=2, blank=True)
    transferdate = models.CharField(max_length=100, blank=True)
    transfertime = models.CharField(max_length=20, blank=True)
    transfertype = models.CharField(max_length=2, blank=True)
    transferwhere = models.CharField(max_length=20, blank=True)
    processid = models.CharField(max_length=4, blank=True)

    class Meta:
        managed = False
        db_table = 'transferplan'


class Ucdgroup(models.Model):
    ucdgroupid = models.CharField(max_length=4)
    ucdgroupname = models.CharField(max_length=30)
    ucdgroupmemo = models.CharField(max_length=60, blank=True)
    ucdgroupdialno = models.CharField(max_length=4, blank=True)
    ucdgroupenterno = models.CharField(max_length=2, blank=True)
    ucdgrouptruncatetype = models.CharField(max_length=2, blank=True)
    ucdlastuserid = models.IntegerField(blank=True, null=True)
    nowpdrs = models.IntegerField(blank=True, null=True)
    ifopen = models.CharField(max_length=2, blank=True)
    ucdtransfertype = models.CharField(max_length=2, blank=True)
    ucdtransfertime = models.CharField(max_length=20, blank=True)
    ucdtransferwhere = models.CharField(max_length=100, blank=True)
    usecustomercallno = models.CharField(max_length=2, blank=True)
    bussinessgroupid = models.CharField(max_length=4, blank=True)

    class Meta:
        managed = False
        db_table = 'ucdgroup'


class Ucdgroupuser(models.Model):
    yhbh = models.CharField(max_length=8)
    ucdgroupid = models.CharField(max_length=4)
    jtdj = models.CharField(max_length=4, blank=True)

    class Meta:
        managed = False
        db_table = 'ucdgroupuser'


class Ucdgroupusernew(models.Model):
    yhbh = models.CharField(max_length=8)
    ucdgroupid = models.CharField(max_length=4)
    jtdj = models.CharField(max_length=4, blank=True)

    class Meta:
        managed = False
        db_table = 'ucdgroupusernew'


class Ucdworkgroup(models.Model):
    groupid = models.CharField(max_length=4)
    groupname = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 'ucdworkgroup'


class VeConfrecordQxb(models.Model):
    userid = models.CharField(max_length=20)
    lx = models.CharField(max_length=20, blank=True)
    hm = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 've_confrecord_qxb'


class VeQxb(models.Model):
    yhbh = models.CharField(max_length=8)
    bh = models.CharField(max_length=8)
    fgsbh = models.CharField(max_length=8)
    zdbh = models.CharField(max_length=8)
    sfsc = models.CharField(max_length=1, blank=True)
    sfzj = models.CharField(max_length=1, blank=True)
    sfbc = models.CharField(max_length=1, blank=True)
    sfdy = models.CharField(max_length=1, blank=True)
    sfsh = models.CharField(max_length=1, blank=True)
    sfcx = models.CharField(max_length=1, blank=True)
    tbm = models.CharField(max_length=1, blank=True)
    cplx = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 've_qxb'


class VeQxbNew(models.Model):
    yhbh = models.CharField(max_length=10)
    qxmc = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 've_qxb_new'


class VeRecordQxb(models.Model):
    userid = models.CharField(max_length=20)
    lx = models.CharField(max_length=20, blank=True)
    hm = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 've_record_qxb'


class VeYhb(models.Model):
    yhbh = models.CharField(max_length=12)
    mc = models.CharField(max_length=20, blank=True)
    mm = models.CharField(max_length=20, blank=True)
    sffz = models.CharField(max_length=1, blank=True)
    ssz = models.CharField(max_length=8, blank=True)
    fgsbh = models.CharField(max_length=8, blank=True)
    zdbh = models.CharField(max_length=8, blank=True)
    cplx = models.CharField(max_length=4, blank=True)
    ygbh = models.CharField(max_length=8, blank=True)
    zt_yh = models.CharField(max_length=1, blank=True)
    ssxz = models.CharField(max_length=8, blank=True)
    calloutno = models.CharField(max_length=20, blank=True)
    outlineid = models.CharField(max_length=20, blank=True)
    sfzj = models.CharField(max_length=1, blank=True)
    calloutgroup = models.CharField(max_length=4, blank=True)
    switchoutno = models.CharField(max_length=20, blank=True)
    calloutuser = models.CharField(max_length=10, blank=True)
    hhsl = models.CharField(max_length=20, blank=True)
    recordflag = models.CharField(max_length=1, blank=True)
    thsl = models.CharField(max_length=50, blank=True)

    class Meta:
        managed = False
        db_table = 've_yhb'


class Voipgroupline(models.Model):
    extno = models.CharField(max_length=4)
    groupkey = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'voipgroupline'
