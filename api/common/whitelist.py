from config.settings import X_ORIGIN_SECRET
from rest_framework.permissions import BasePermission


class HeaderWhitelist(BasePermission):
    secret = X_ORIGIN_SECRET

    def has_permission(self, request, view):
        return request.META.get('HTTP_X_ORIGIN_SECRET', None) == self.secret
