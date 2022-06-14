from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from django.contrib.auth.models import User 
from rest_framework.request import Request
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from .models import Message ,Services,Rating                                                  
from .serializers import MessageSerializer, RatingSerializerView, UserSerializer ,ServiceSerializer, RatingSerializer



@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def list_all_message(request):
    messages = Message.objects.all()
    serializer = MessageSerializer(messages, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def message_list(request,id):
    messages = Message.objects.filter(id=id)
    serializer = MessageSerializer(messages, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def create_message(request : Request):
    data = JSONParser().parse(request)
    serializer = MessageSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_service(request : Request):
    ''' add service by Tour guide'''
    account= request.user
    if not account.is_authenticated or not account.has_perm('chatApp.add_services'):
        return Response("You Don't Have Permission To add That", status = 400)
    request.data["user"] = request.user.id
    serializer = ServiceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        dataResponse = {
            "msg" : "Created service Successfully",
            "post" : serializer.data}
        return Response(dataResponse)
    else:
        print(serializer.errors)
        dataResponse = {"msg" : "couldn't create a service"}
        return Response( dataResponse, status=400)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes((IsAuthenticated,))
def update_service(request : Request, id):
    '''update service by creator'''
    service = Services.objects.get(id=id)
    user=request.user
    if service.user != user:
        return Response({'response':"You Don't Have Permission To Edit That"})
    request.data["user"] = request.user.id
    updated_service = ServiceSerializer(instance=service, data=request.data)
    if updated_service.is_valid():
        updated_service.save()
        responseData = {
            "msg" : "updated successefully"
        }

        return Response(responseData)
    else:
        print(updated_service.errors)
        return Response({"msg" : "bad request, cannot update"}, status=400)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def list_services_by_TourGuide(request : Request,user_id):
    '''list all services for TourGuide'''
   # user=User.objects.get(username)
    services = Services.objects.filter(user_id=user_id)

    dataResponse = {
        "msg" : "List of All servises",
        "services" : ServiceSerializer(instance=services, many=True).data
        }

    return Response(dataResponse)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def list_all_services(request : Request):
    '''list all services '''
    services = Services.objects.all()

    dataResponse = {
        "msg" : "List of All servises",
        "services" : ServiceSerializer(instance=services, many=True).data
        }

    return Response(dataResponse)

@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_service(request: Request, id):
    '''Delete service by creator '''
    service = Services.objects.get(id=id)
    user=request.user
    if  service.user != user:
        return Response({'response':"You Don't Have Permission To Delete That"})
    service.delete()
    return Response({"msg" : "Deleted Successfully"})



@api_view(['post'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_rate(request : Request):
    ''' add rate for service'''
    account= request.user
    if not account.is_authenticated or not account.has_perm('chatApp.add_rating'):
        return Response("You Don't Have Permission To add That", status = 400)
    request.data["client_user"] = request.user.id
    serializer = RatingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        dataResponse = {
            "msg" : "send Rate Successfully",
            "rate" : serializer.data}
        return Response(dataResponse)
    else:
        print(serializer.errors)
        dataResponse = {"msg" : "couldn't send a Rate"}
        return Response( dataResponse, status=400)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def list_Rate(request : Request,user_id):
    '''list all rating '''
    user=request.user
    if not user.has_perm('chatApp.view_rating'):
        return Response("You Don't Have Permission To add That", status = 400)
    rate = Rating.objects.filter(service__user__id=user_id)
    dataResponse = {
        "msg" : "List of rate",
        "rate" : RatingSerializerView(instance=rate, many=True).data
        }

    return Response(dataResponse)











'''# Users View
@csrf_exempt  # Decorator to make the view csrf excempt.
def user_list(request, pk=None):
    """List all required messages, or create a new message."""
    if request.method == 'GET':
        if pk: # If PrimaryKey (id) of the user is specified in the url
            users = User.objects.filter(id=pk) # Select only that particular user
        else:
            users = User.objects.all()
        serializer = UserSerializer(users, many=True, context={'request': request}) 
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request) # On POST, parse the request object to obtain the data in json
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()      
            return JsonResponse(serializer.data, status=201) 
        return JsonResponse(serializer.errors, status=400) '''