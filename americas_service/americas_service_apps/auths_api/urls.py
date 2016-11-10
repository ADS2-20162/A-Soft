from django.conf.urls import url, include
from rest_framework import routers
# from rest_framework_extensions.routers import ExtendedSimpleRouter
from .views.permission_view import PermissionViewSet

from .views.menu_view import MenuViewSet
from .views.user_view import UserViewSet, LocalUserInfoView
from .views.api_user_menu import UserMenuView
from .views.api_logs import LogView
from .views.api_routers import RouterView


# from .api_views import load_menu

router = routers.DefaultRouter()

router.register(r'permissions', PermissionViewSet)

router.register(r'users', UserViewSet)

router.register(r'menus', MenuViewSet)


urlpatterns = [

    url(r'^localuserinfo/$', LocalUserInfoView.as_view()),
    # url(r'^load_menu/$', load_menu, name='load_menu'),
    url(r'^usermenu/$', UserMenuView.as_view()),
    url(r'^logs/(?P<param>[^/]+)/$', LogView.as_view()),

    url(r'^routers/$', RouterView.as_view()),

    url(r'^', include(router.urls)),
]
