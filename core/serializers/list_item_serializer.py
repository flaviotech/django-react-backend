from rest_framework import serializers

from ..models import ListItem


class ListItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ListItem
        fields = [
            'id',
            'url',
            'name',
            'done',
            'list',
        ]
