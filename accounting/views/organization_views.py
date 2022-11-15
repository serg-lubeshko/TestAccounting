from rest_framework import generics
from rest_framework.exceptions import NotFound

from accounting.models import Organization
from accounting.permission.permissions import IsAnAuthor
from accounting.serializers.organization_serializers import OrganizationSerializer


class OrganizationListCreate(generics.ListCreateAPIView):
    serializer_class = OrganizationSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        return context

    def get_queryset(self):
        user = self.request.user
        try:
            queryset = Organization.objects.filter(user=user)
        except Exception:
            raise NotFound()
        return queryset


class OrganizationRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    lookup_url_kwarg = 'org_id'
    serializer_class = OrganizationSerializer
    permission_classes = [IsAnAuthor]
