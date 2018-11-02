from django.db import models
import datetime

class Environment(models.Model):
    name = models.CharField(max_length=64)
    dbHost = models.CharField(max_length=64)
    dbName = models.CharField(max_length=64)
    dbUsername = models.CharField(max_length=64)
    dbPassword = models.CharField(max_length=128)
    dbProt = models.IntegerField()
    createTime = models.DateTimeField(default=datetime.datetime.now())


    def __unicode__(self):
        return self.name,self.dbHost,self.dbName,self.dbUsername,self.dbPassword,self.dbProt
    # class Meta:
    #     db_table = 'environment'  # 自定义表名称为mytable
    #     app_label = ''
    #
    # def __unicode__(self):
    #     return self.name

# class dbmethod(models.Model):
#     id = models.IntegerField()
#     name = models.CharField(max_length=50)
#     class Meta:
#         db_table = 'dbmethod'  # 自定义表名称为mytable
#         app_label = ''
#
#
# class fields(models.Model):
#     id = models.IntegerField()
#     tableId =  models.IntegerField()
#     name = models.CharField(max_length=50)
#     class Meta:
#         db_table = 'fields'  # 自定义表名称为mytable
#         app_label = ''
#
# class tables(models.Model):
#     id = models.IntegerField()
#     name = models.CharField(max_length=50)
#     class Meta:
#         db_table = 'tables'  # 自定义表名称为mytable
#         app_label = ''