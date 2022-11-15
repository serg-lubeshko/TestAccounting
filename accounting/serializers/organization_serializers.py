from rest_framework import serializers

from accounting.models import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    organization_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Organization
        fields = (
            'organization_id',
            'organization_name',
        )

    def create(self, validated_data):
        user = self.context['user']
        return Organization.objects.create(**validated_data | {'user': user})
