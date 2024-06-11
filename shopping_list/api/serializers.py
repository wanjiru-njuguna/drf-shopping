from rest_framework import serializers

from shopping_list.models import ShoppingItem, ShoppingList
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):  # NEW!
    class Meta:
        model = User
        fields = ["id", "username"]


class ShoppingItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingItem
        fields = ["id", "name", "purchased"]
        read_only_fields = ('id',)
    def create(self, validated_data, **kwargs):
        validated_data['shopping_list_id'] = self.context['request'].parser_context['kwargs']['pk']
        return super(ShoppingItemSerializer, self).create(validated_data)

class ShoppingListSerializer(serializers.ModelSerializer):
    shopping_items = ShoppingItemSerializer(many=True, read_only=True)
    members = UserSerializer(many=True, read_only=True)

    class Meta:
        model = ShoppingList
        fields = ['id', 'name', 'shopping_items', 'members']