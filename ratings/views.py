from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ratings.models import Rating
from ratings.serializers import RatingSerializer

@api_view(['GET'])
def average_rating_for_zipcode(request, zipcode):
    """
    Get average rating values for zipcode.
    """
    ratings = Rating.objects.filter(zipcode=zipcode)
    ratings_count = ratings.count()

    if(ratings_count == 0):
    	return Response(status=status.HTTP_404_NOT_FOUND)

    # Get all rated values
    total_sum = 0.0
    culture_sum = 0.0
    infrastructure_sum = 0.0
    green_sum = 0.0
    safety_sum = 0.0
    for rating in ratings:
    	total_sum += rating.total
    	culture_sum += rating.culture
    	infrastructure_sum += rating.infrastructure
    	green_sum += rating.green
    	safety_sum += rating.safety

    # Get rounded average values
    total_average = int(round(total_sum / ratings_count))
    culture_average = int(round(culture_sum / ratings_count))
    infrastructure_average = int(round(infrastructure_sum / ratings_count))
    green_average = int(round(green_sum / ratings_count))
    safety_average = int(round(safety_sum / ratings_count))

    # Create a new Rating object with average values
    average_rating = Rating(zipcode=zipcode, user_id='average', 
    	total=total_average, culture=culture_average, infrastructure=infrastructure_average,
    	green=green_average, safety=safety_average)

    serializer = RatingSerializer(average_rating)
    return Response(serializer.data)


@api_view(['GET'])
def ratings_for_zipcode(request, zipcode):
    """
    List all code ratings.
    """
    ratings = Rating.objects.filter(zipcode=zipcode)
    serializer = RatingSerializer(ratings, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def create_or_update_rating(request):
    """
    Create new or update existing rating.
    """
    if request.method == 'POST':
        data = request.data
        try:
        	# Search for rating
        	rating = Rating.objects.get(user_id=data.get('user_id'), zipcode=data.get('zipcode'))
        	serializer = RatingSerializer(rating, data=data)
        	http_status = status.HTTP_200_OK
    	except Rating.DoesNotExist:
    		# Nothing to update, create new
        	serializer = RatingSerializer(data=data)
        	http_status = status.HTTP_201_CREATED

        # Validate data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=http_status)
        # Data not valid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def all_ratings(request):
    """
    List all existing ratings.
    """
    ratings = Rating.objects.all()
    serializer = RatingSerializer(ratings, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE'])
def single_rating(request, user_id, zipcode):
    """
    Retrieve or delete a single rating.
    """
    try:
        rating = Rating.objects.get(user_id=user_id, zipcode=zipcode)
    except Rating.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RatingSerializer(rating)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        rating.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

