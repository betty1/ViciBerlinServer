from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from ratings.models import Rating
from ratings.serializers import RatingSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def create_or_update_rating(request):
    """
    Create new or update existing rating.
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        try:
        	# Search for rating
        	rating = Rating.objects.get(user_id=data.get('user_id'), zipcode=data.get('zipcode'))
        	serializer = RatingSerializer(rating, data=data)
        	status = 200
    	except Rating.DoesNotExist:
    		# Nothing to update, create new
        	serializer = RatingSerializer(data=data)
        	status = 201

        # Validate data
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=status)
        # Data not valid
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def all_ratings(request):
    """
    List all code ratings.
    """
    ratings = Rating.objects.all()
    serializer = RatingSerializer(ratings, many=True)
    return JSONResponse(serializer.data)

@csrf_exempt
def single_rating(request, user_id, zipcode):
    """
    Retrieve or delete a single rating.
    """
    try:
        rating = Rating.objects.get(user_id=user_id, zipcode=zipcode)
    except Rating.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RatingSerializer(rating)
        return JSONResponse(serializer.data)

    elif request.method == 'DELETE':
        rating.delete()
        return HttpResponse(status=204)

