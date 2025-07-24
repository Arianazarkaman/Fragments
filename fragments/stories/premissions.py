from rest_framework.permissions import BasePermission, IsAuthenticated

class IsPremiumUser(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.groups.filter(name='premium_users').exists():
            return True
        return False
