from rest_framework import permissions


class IsObjectOwner(permissions.BasePermission):
    """
    Checks if the requesting user is the owner of the object.
    """
    def has_object_permission(self, request, view, obj):
        """
        Returns True if the requesting user is the owner of the object,
        otherwise returns False.
        """
        if obj.user == request.user:
            return True
        else:
            return False
