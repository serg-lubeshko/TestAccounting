from rest_framework.permissions import BasePermission


class IsAnAuthor(BasePermission):
    message = 'Editing category is restricted to the author only.'

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user