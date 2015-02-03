# coding=utf-8
from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from rest_framework.authtoken.views import obtain_auth_token

from robothub.urls import router


urlpatterns = [
    url(r'^api/token/', obtain_auth_token, name='api-token'),
    url(r'^api/', include(router.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
]

urlpatterns += staticfiles_urlpatterns()