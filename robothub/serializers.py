from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Suite, Test, Test_Status, Application, Project, Keyword, Tag, Test_Run, Test_Run_Status, \
    Test_Run_Error, Tag_Status, Suite_Status, Keyword_Status


class TagSerializer(serializers.ModelSerializer):
    # assigned = serializers.SlugRelatedField(slug_field=User.USERNAME_FIELD, required=False)
    # status_display = serializers.SerializerMethodField('get_status_display')

    links = serializers.SerializerMethodField()
    test = serializers.HyperlinkedRelatedField(read_only=True, view_name='test-detail')

    class Meta:
        model = Tag
        fields = ('id', 'content', 'test', 'links')

    def get_status_display(self, obj):
        return obj.get_status_display()

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('tag-detail',
                            kwargs={'pk': obj.pk}, request=request),
        }
class TestRunSerializer(serializers.ModelSerializer):
    # assigned = serializers.SlugRelatedField(slug_field=User.USERNAME_FIELD, required=False)
    # status_display = serializers.SerializerMethodField('get_status_display')

    links = serializers.SerializerMethodField()

    class Meta:
        model = Test_Run
        fields = ('id', 'started_at', 'finished_at', 'source_file', 'hash', 'imported_at', 'links')

    def get_status_display(self, obj):
        return obj.get_status_display()

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('test_run-detail',
                            kwargs={'pk': obj.pk}, request=request),
        }

class TagStatusSerializer(serializers.ModelSerializer):
    # assigned = serializers.SlugRelatedField(slug_field=User.USERNAME_FIELD, required=False)
    # status_display = serializers.SerializerMethodField('get_status_display')

    links = serializers.SerializerMethodField()
    test_run = serializers.HyperlinkedRelatedField(read_only=True, view_name='test_run-detail')

    class Meta:
        model = Tag_Status
        fields = ('id', 'passed', 'name', 'failed', 'elapsed','critical', 'links', 'test_run')

    def get_status_display(self, obj):
        return obj.get_status_display()

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('tag_status-detail',
                            kwargs={'pk': obj.pk}, request=request),
        }




class TestRunStatusSerializer(serializers.ModelSerializer):
    # assigned = serializers.SlugRelatedField(slug_field=User.USERNAME_FIELD, required=False)
    # status_display = serializers.SerializerMethodField('get_status_display')

    links = serializers.SerializerMethodField()
    test_run = serializers.HyperlinkedRelatedField(read_only=True, view_name='test_run-detail')

    class Meta:
        model = Test_Run_Status
        fields = ('id', 'passed', 'name', 'failed', 'elapsed', 'links', 'test_run')

    def get_status_display(self, obj):
        return obj.get_status_display()

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('test_run_status-detail',
                            kwargs={'pk': obj.pk}, request=request),
        }


class TestRunErrorSerializer(serializers.ModelSerializer):
    # assigned = serializers.SlugRelatedField(slug_field=User.USERNAME_FIELD, required=False)
    # status_display = serializers.SerializerMethodField('get_status_display')

    links = serializers.SerializerMethodField()
    test_run = serializers.HyperlinkedRelatedField(read_only=True, view_name='test_run-detail')

    class Meta:
        model = Test_Run_Error
        fields = ('id', 'content', 'timestamp', 'level', 'links', 'test_run')

    def get_status_display(self, obj):
        return obj.get_status_display()

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('test_run_error-detail',
                            kwargs={'pk': obj.pk}, request=request),
        }


class KeywordSerializer(serializers.ModelSerializer):
    # assigned = serializers.SlugRelatedField(slug_field=User.USERNAME_FIELD, required=False)
    # status_display = serializers.SerializerMethodField('get_status_display')

    links = serializers.SerializerMethodField()
    test = serializers.HyperlinkedRelatedField(read_only=True, view_name='test-detail')
    suite = serializers.HyperlinkedIdentityField(read_only=True, view_name='suite-detail')

    class Meta:
        model = Keyword
        fields = ('id', 'name', 'doc', 'timeout', 'type', 'links', 'test', 'suite')

    def get_status_display(self, obj):
        return obj.get_status_display()

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('keyword-detail',
                            kwargs={'pk': obj.pk}, request=request),
        }

class KeywordStatusSerializer(serializers.ModelSerializer):
    # assigned = serializers.SlugRelatedField(slug_field=User.USERNAME_FIELD, required=False)
    # status_display = serializers.SerializerMethodField('get_status_display')

    links = serializers.SerializerMethodField()
    keyword = serializers.HyperlinkedRelatedField(read_only=True, view_name='keyword-detail')
    test_run = serializers.HyperlinkedIdentityField(read_only=True, view_name='test_run-detail')

    class Meta:
        model = Keyword_Status
        fields = ('id', 'status', 'elapsed', 'keyword','test_run', 'links')

    def get_status_display(self, obj):
        return obj.get_status_display()

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('keyword_status-detail',
                            kwargs={'pk': obj.pk}, request=request),
        }


class Test_StatusSerializer(serializers.ModelSerializer):
    # assigned = serializers.SlugRelatedField(slug_field=User.USERNAME_FIELD, required=False)
    # status_display = serializers.SerializerMethodField('get_status_display')

    links = serializers.SerializerMethodField()
    test = serializers.HyperlinkedRelatedField(read_only=True, view_name='test-detail')

    class Meta:
        model = Test_Status
        fields = ('id', 'status', 'elapsed', 'links', 'test',)

    def get_status_display(self, obj):
        return obj.get_status_display()

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('test_status-detail',
                            kwargs={'pk': obj.pk}, request=request),
        }


class TestSerializer(serializers.ModelSerializer):
    # assigned = serializers.SlugRelatedField(slug_field=User.USERNAME_FIELD, required=False)
    # status_display = serializers.SerializerMethodField('get_status_display')

    links = serializers.SerializerMethodField()
    suite = serializers.HyperlinkedRelatedField(read_only=True, view_name='suite-detail')
    test_status = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='test_status-detail')

    class Meta:
        model = Test
        fields = ('id', 'xml_id', 'name', 'doc', 'timeout', 'links', 'suite', 'test_status',)

    def get_status_display(self, obj):
        return obj.get_status_display()

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('test-detail',
                            kwargs={'pk': obj.pk}, request=request),
        }


class SuiteSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()
    tests = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='test-detail')
    application = serializers.HyperlinkedRelatedField(read_only=True, view_name='application-detail')

    class Meta:
        model = Suite
        fields = ('id', 'source', 'xml_id', 'name', 'doc', 'links', 'tests', 'application')

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('suite-detail',
                            kwargs={'pk': obj.pk}, request=request),
        }

class SuiteStatusSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()
    test_run = serializers.HyperlinkedRelatedField(read_only=True, view_name='test_run-detail')
    suite = serializers.HyperlinkedRelatedField(read_only=True, view_name='suite-detail')

    class Meta:
        model = Suite_Status
        fields = ('id', 'status', 'failed', 'elapsed', 'passed', 'links', 'test_run', 'suite')

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('suite-detail',
                            kwargs={'pk': obj.pk}, request=request),
        }

class ProjectSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()
    applications = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='application-detail')

    class Meta:
        model = Project
        fields = ('id', 'project_name', 'links', 'applications',)

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('project-detail',
                            kwargs={'pk': obj.pk}, request=request),
        }


class ApplicationSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()
    project = serializers.HyperlinkedRelatedField(read_only=True, view_name='project-detail')
    suites = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='suite-detail')

    class Meta:
        model = Application
        fields = ('id', 'application_name', 'framework_name', 'git_link', 'jira_link', 'links', 'project', 'suites',)

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('application-detail',
                            kwargs={'pk': obj.pk}, request=request),
        }


