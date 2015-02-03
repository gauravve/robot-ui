from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'project', views.ProjectViewSet)
router.register(r'application', views.ApplicationViewSet)
router.register(r'suite', views.SuiteViewSet)
router.register(r'suitestatus', views.SuiteStatusViewSet)
router.register(r'test', views.TestViewSet)
router.register(r'test_status', views.TestStatusViewSet)
router.register(r'keyword', views.KeywordViewSet)
router.register(r'keyword_status', views.KeywordStatusViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'tagstatus', views.TagStatusViewSet)
router.register(r'testrun', views.TestRunViewSet)
router.register(r'testrunstatus', views.TestRunStatusViewSet)
router.register(r'testrunerror', views.TestRunErrorViewSet)





