from rest_framework import serializers

from drugs.models import Drug, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class DrugSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset = Category.objects.all(),
        source='category',
        write_only=True
    )
    class Meta:
        model = Drug
        fields = ['id', 'name', 'description', 'price', 'category', 'category_id']
