"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from studies.views import testView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studies/v1/', testView.as_view()),
]

schema_view = get_schema_view(
    openapi.Info(
        title="Humanscape API Document",
        default_version='v1',
        description=
        """
        휴먼스케이프 기업과제 api 명세서 페이지입니다.
        """,
    ),
    validators=['flex'],
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('studies.urls'))
]

urlpatterns += [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
<<<<<<< HEAD
]
=======
]


>>>>>>> 82150ba107f3d851a3a3f78b65514b7e9ea8a2c7
