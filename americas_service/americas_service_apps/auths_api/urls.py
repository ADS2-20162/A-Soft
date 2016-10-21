from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_extensions.routers import ExtendedSimpleRouter

from americas_service_apps.auths_api.views.PermissionView import PermissionViewSet

from americas_service_apps.auths_api.views.MenuView import MenuViewSet
from americas_service_apps.auths_api.views.UserView import UserViewSet, LocalUserInfoView
from americas_service_apps.auths_api.views.UserMenuView import UserMenuView


# from .api_views import load_menu

router = routers.DefaultRouter()

router.register(r'permissions', PermissionViewSet)

router.register(r'users', UserViewSet)

router.register(r'menus', MenuViewSet)


urlpatterns = [

    url(r'^localuserinfo/$', LocalUserInfoView.as_view()),
    # url(r'^load_menu/$', load_menu, name='load_menu'),
    url(r'^usermenu/$', UserMenuView.as_view()),

    url(r'^', include(router.urls)),
]
