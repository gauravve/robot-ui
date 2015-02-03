from rest_framework import authentication, permissions, viewsets

from .models import Suite, Test, Test_Status, Application, Project, Keyword, Tag, Test_Run, Test_Run_Status, \
    Test_Run_Error, Tag_Status, Suite_Status, Keyword_Status
from .serializers import SuiteSerializer, TestSerializer, Test_StatusSerializer, ApplicationSerializer, \
    ProjectSerializer, KeywordSerializer, TagSerializer, TestRunSerializer, TestRunStatusSerializer, \
    TestRunErrorSerializer, TagStatusSerializer, SuiteStatusSerializer, KeywordStatusSerializer


class DefaultsMixin(object):
    """Default settings for view authentication, permissions,
    filtering and pagination."""

    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100


class SuiteViewSet(viewsets.ModelViewSet):
    queryset = Suite.objects.order_by('id')
    serializer_class = SuiteSerializer


class SuiteStatusViewSet(viewsets.ModelViewSet):
    queryset = Suite_Status.objects.order_by('id')
    serializer_class = SuiteStatusSerializer


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.order_by('id')
    serializer_class = TestSerializer


class TestStatusViewSet(viewsets.ModelViewSet):
    queryset = Test_Status.objects.order_by('id')
    serializer_class = Test_StatusSerializer


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.order_by('id')
    serializer_class = ApplicationSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.order_by('id')
    serializer_class = ProjectSerializer


class KeywordViewSet(viewsets.ModelViewSet):
    queryset = Keyword.objects.order_by('id')
    serializer_class = KeywordSerializer

class KeywordStatusViewSet(viewsets.ModelViewSet):
    queryset = Keyword_Status.objects.order_by('id')
    serializer_class = KeywordStatusSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.order_by('id')
    serializer_class = TagSerializer


class TagStatusViewSet(viewsets.ModelViewSet):
    queryset = Tag_Status.objects.order_by('id')
    serializer_class = TagStatusSerializer


class TestRunViewSet(viewsets.ModelViewSet):
    queryset = Test_Run.objects.order_by('id')
    serializer_class = TestRunSerializer


class TestRunStatusViewSet(viewsets.ModelViewSet):
    queryset = Test_Run_Status.objects.order_by('id')
    serializer_class = TestRunStatusSerializer


class TestRunErrorViewSet(viewsets.ModelViewSet):
    queryset = Test_Run_Error.objects.order_by('id')
    serializer_class = TestRunErrorSerializer