from rest_framework import serializers
from ratings.models import Rating

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'user_id', 'zipcode', 'last_modified', 'total', 'culture', 'infrastructure',
                'green', 'safety')

# class RatingSerializer(serializers.Serializer):
#     user_id = serializers.CharField(max_length=200)
#     zipcode = serializers.CharField(max_length=5)
#     total = serializers.IntegerField(default=3, required=False)
#     culture = serializers.IntegerField(default=3)
#     infrastructure = serializers.IntegerField(default=3)
#     green = serializers.IntegerField(default=3)
#     safety = serializers.IntegerField(default=3)

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Rating.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Rating` instance, given the validated data.
#         """
#         instance.user_id = validated_data.get('user_id', instance.user_id)
#         instance.zipcode = validated_data.get('zipcode', instance.zipcode)
#         instance.total = validated_data.get('total', instance.total)
#         instance.culture = validated_data.get('culture', instance.culture)
#         instance.infrastructure = validated_data.get('infrastructure', instance.infrastructure)
#         instance.green = validated_data.get('green', instance.green)
#         instance.safety = validated_data.get('safety', instance.safety)
#         instance.save()
#         return instance