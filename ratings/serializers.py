from rest_framework import serializers
from ratings.models import Rating

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'user_id', 'zipcode', 'last_modified', 'total', 'culture', 'infrastructure',
                'green', 'safety')