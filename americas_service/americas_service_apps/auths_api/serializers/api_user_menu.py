# import the logging library
import logging
from django.utils.encoding import force_text
from rest_framework import serializers
# from django.db.models import Q
# from operator import __or__ as OR
# from functools import reduce
from rest_framework.response import Response
# from rest_framework.decorators import detail_route, list_route
from rest_framework import permissions
# from rest_framework import decorators
from rest_framework.views import APIView
from rest_framework import status
# from americas_service_apps.utils.serializers import RecursiveSerializer
# from americas_service_apps.utils.pagination import LocalPagination
from americas_service_apps.utils.security import log_params
from americas_service_apps.utils.permissions import ModelPermission
from django.db.models import Q

from django.contrib.auth.models import Group, Permission
from americas_service_apps.auths.models.Hierarchy import Hierarchy
from americas_service_apps.auths.models.Menu import Menu
from americas_service_apps.auths.models.UserHierarchyGroup import UserHierarchyGroup
from americas_service_apps.auths.models.UserHierarchyPermission import \
    UserHierarchyPermission
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.utils.six import BytesIO
# Get an instance of a logger
log = logging.getLogger(__name__)


class CustomSerializer(serializers.BaseSerializer):

    def to_representation(self, obj):
        return {
            'id': str(obj.id),
            'module': obj.module,
            'title': obj.title,
            'type': obj.type,
            'parent_title': obj.parent.title,  # for data: { section: 'System',
            # page: 'Categoría' },
        }


class MenuInfoSerializer(serializers.ModelSerializer):
    # menu_items = serializers.ListField()

    class Meta:
        model = Menu
        # fields = ('id', 'module', 'title', 'type', 'menu_items')

    def to_representation(self, obj):
        return {
            'title': obj.title,
            # 'type': obj.type,
            'type': 'link' if obj.parent else 'toggle',
            'module': obj.module,
            'state': obj.state,
            'menu_items': [],
            'parent_title': obj.parent.title if obj.parent else '',
            # 'id': str(obj.id),

        }
