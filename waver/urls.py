"""waver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.urls import re_path
from waverapi.views import register_user, login_user
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework import routers
from waverapi.views.waver_user_view import WaverUserView
from waverapi.views.gear_view import GearView
from waverapi.views.gear_type_view import GearTypeView
from waverapi.views.manufacturer_view import ManufacturerView
from waverapi.views.specification_view import SpecificationView
from waverapi.views.review_view import ReviewView
from waverapi.views.used_gear_view import UsedGearView
from waverapi.views.post_view import PostView

schema_view = get_schema_view(
    openapi.Info(
        title="Waver API",
        default_version='v1',
        description="API for Synthesizer enthusiasts",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@waver.local"),
        license=openapi.License(name="BSD License"),
    ),

    public=True,
    permission_classes=[permissions.AllowAny],
)





router = routers.DefaultRouter(trailing_slash=False)
router.register(r'waver_users', WaverUserView, 'waver_user')
router.register(r'gear', GearView, 'gear')
router.register(r'gear_type', GearTypeView, 'gear_type')
router.register(r'manufacturers', ManufacturerView, 'manufacturer')
router.register(r'specifications', SpecificationView, 'specification')
router.register(r'reviews', ReviewView, 'review')
router.register(r'used_gear', UsedGearView, 'used_gear')
router.register(r'posts', PostView, 'post')








# router.register(r'tickets', TicketView, 'serviceTicket')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('swagger', schema_view.with_ui('swagger',
            cache_timeout=0), name='schema-swagger-ui'),
]
