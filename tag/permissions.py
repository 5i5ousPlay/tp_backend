from rest_framework.permissions import BasePermission


class IsTagCreatorOrIsAdmin(BasePermission):
    """
    Checks if request user is the same
    as the author of the review or if
    user is super_user.
    """
    def has_object_permission(self, request, view, obj):
        return (obj.creator == request.user) | (request.user and request.user.is_superuser)
