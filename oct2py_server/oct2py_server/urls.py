"""oct2py_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework.schemas import get_schema_view

rest_api_urls = [
    url(r'^$', get_schema_view()),
    url(r'^auth/token/obtain/$', obtain_jwt_token),
    url(r'^auth/token/refresh/$', refresh_jwt_token),
    url(r'^scripts/', include('scripts.api.urls', namespace='api-scripts')),
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(rest_api_urls, namespace='rest-api')),
    url(r'^(?P<path>.*)', include('scripts.urls', namespace='front-end')),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
