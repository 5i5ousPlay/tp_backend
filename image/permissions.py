from rest_framework import permissions


class IsImageOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.uploaded_by == request.user
