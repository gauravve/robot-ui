# coding=utf-8
from django.db import models

# Create your models here.

class Project(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    project_name = models.CharField(max_length=100)


class Application(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    application_name = models.CharField(max_length=100)
    framework_name = models.CharField(max_length=200)
    jira_link = models.CharField(max_length=200, )
    git_link = models.CharField(max_length=200)
    project = models.ForeignKey(Project, related_name='applications', default=1)


class Suite(models.Model):
    id = models.IntegerField(primary_key=True)
    suite_id = models.CharField(max_length=20,blank=True,null=True)
    source = models.CharField(max_length=500)
    xml_id = models.CharField(max_length=20)
    name = models.CharField(max_length=500)
    doc = models.CharField(max_length=2000)
    application = models.ForeignKey(Application, related_name='suites', null=True)


class Test(models.Model):
    id = models.IntegerField(primary_key=True)
    xml_id = models.CharField(max_length=20)
    name = models.CharField(max_length=500)
    doc = models.CharField(max_length=2000)
    timeout = models.CharField(max_length=10)
    suite = models.ForeignKey(Suite, related_name='tests')


class Keyword(models.Model):
    id = models.IntegerField(primary_key=True)
    keyword_id = models.CharField(max_length=20,blank=True,null=True)
    name = models.CharField(max_length=500)
    doc = models.CharField(max_length=500)
    timeout = models.CharField(max_length=10)
    type = models.CharField(max_length=20)
    test = models.ForeignKey(Test, related_name='keywords', null=True)
    suite = models.ForeignKey(Suite, related_name='keywords', null=True)


class Tag(models.Model):
    id = models.IntegerField(primary_key=True)
    content = models.CharField(max_length=200)
    test = models.ForeignKey(Test, related_name='tags')

class Test_Run(models.Model):
    id = models.IntegerField(primary_key=True)
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField()
    source_file = models.CharField(max_length=500)
    hash = models.CharField(max_length=50)
    imported_at = models.DateTimeField()


class Test_Status(models.Model):
    id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=20)
    elapsed = models.IntegerField()
    test = models.ForeignKey(Test, related_name='test_status')
    test_run = models.ForeignKey(Test_Run,related_name='test_status')


class Test_Run_Error(models.Model):
    id = models.IntegerField(primary_key=True)
    content = models.CharField(max_length=500)
    timestamp = models.DateTimeField()
    level = models.CharField(max_length=20)
    test_run = models.ForeignKey(Test_Run,related_name='test_run')


class Test_Run_Status(models.Model):
    id = models.IntegerField(primary_key=True)
    passed = models.IntegerField()
    name = models.CharField(max_length=500)
    failed = models.IntegerField()
    elapsed = models.IntegerField()
    test_run = models.ForeignKey(Test_Run,related_name='test_run_status')


class Tag_Status(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=500)
    failed = models.IntegerField()
    elapsed = models.IntegerField()
    critical = models.IntegerField()
    passed = models.IntegerField()
    test_run = models.ForeignKey(Test_Run,related_name='tag_status')


class Suite_Status(models.Model):
    id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=500)
    failed = models.IntegerField()
    elapsed = models.IntegerField()
    passed = models.IntegerField()
    test_run = models.ForeignKey(Test_Run,related_name='suite_status')
    suite = models.ForeignKey(Suite, related_name='suite_status')


class Keyword_Status(models.Model):
    id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=500)
    elapsed = models.IntegerField()
    test_run = models.ForeignKey(Test_Run,related_name='keyword_status')
    keyword = models.ForeignKey(Keyword, related_name='keyword_status')


class Argument(models.Model):
    id = models.IntegerField(primary_key=True)
    keyword = models.ForeignKey(Keyword, related_name='arguments')
    content = models.CharField(max_length=500)


class Message(models.Model):
    id = models.IntegerField(primary_key=True)
    keyword = models.ForeignKey(Keyword, related_name='messages')
    content = models.CharField(max_length=500)
    timestamp = models.DateTimeField()
    level = models.CharField(max_length=20)





