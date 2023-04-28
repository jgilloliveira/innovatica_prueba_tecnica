from rest_framework import permissions


class IsApprovedPermission(permissions.IsAuthenticated):
    """Permiso si usuaario es aprobado"""

    def has_permission(self, request, view):
        is_authenticated = super().has_permission(request, view)
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return is_authenticated and request.user.is_approved
        elif request.method == 'GET':
            return True

        return is_authenticated
