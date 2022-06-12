from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import City,Profile,Post,Comment
from .serializers import CitySerializer,PostSerializer,ProfileSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_city(request : Request):
    ''' add city by editors'''
    account= request.user
    if not account.is_authenticated or not account.has_perm('QueqibApp.add_city'):
        return Response("Not Allowed", status = status.HTTP_400_BAD_REQUEST)
    new_city=City(user=account)
    if request.method == "POST":
        serializer = CitySerializer(new_city,data=request.data)
    if serializer.is_valid():
        serializer.save()
        dataResponse = {
            "msg" : "Created Ciyt Successfully",
            "post" : serializer.data}
        return Response(dataResponse)
    else:
        print(serializer.errors)
        dataResponse = {"msg" : "couldn't create a City"}
        return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_city(request : Request, slug):
    '''update city inform by editors'''
    account= request.user
    if not account.is_authenticated or not account.has_perm('QueqibApp.change_city'):
        return Response("Not Allowed", status = status.HTTP_400_BAD_REQUEST)
    city = City.objects.get(slug=slug)
    print(request.user.id)
    updated_city = CitySerializer(instance=city, data=request.data)
    if updated_city.is_valid():
        updated_city.save()
        responseData = {
            "msg" : "updated successefully"
        }

        return Response(responseData)
    else:
        print(updated_city.errors)
        return Response({"msg" : "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def list_city(request : Request):
    '''list all city'''
    cities = City.objects.all()

    dataResponse = {
        "msg" : "List of All cities",
        "cities" : CitySerializer(instance=cities, many=True).data
        }

    return Response(dataResponse)

@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_city(request: Request, slug):
    '''Delete city by editors'''
    account= request.user
    if not account.is_authenticated or not account.has_perm('QueqibApp.delete_city'):
        return Response("Not Allowed", status = status.HTTP_400_BAD_REQUEST)
    city = City.objects.get(slug=slug)
    city.delete()
    return Response({"msg" : "Deleted Successfully"})


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_profile(request : Request):
    ''' create profile by Tour guide'''
    print(request.user.id)
    user= request.user
    if not user.is_authenticated or not user.has_perm('QueqibApp.add_profile'):
        return Response("You Don't Have Permission to Create Profile", status = status.HTTP_400_BAD_REQUEST)
    new_profile=Profile(user=user)
    if request.method == "POST":
        serializer = ProfileSerializer(new_profile,data=request.data)
    if serializer.is_valid():
        serializer.save()
        dataResponse = {
            "msg" : "Created profile Successfully",
            "profile" : serializer.data}
        return Response(dataResponse)
    else:
        print(serializer.errors)
        dataResponse = {"msg" : "couldn't create a profile"}
        return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def list_profile(request : Request):
    '''list all profile'''
    profiles = Profile.objects.all()

    dataResponse = {
        "msg" : "List of All profiles",
        "profile" : ProfileSerializer(instance=profiles, many=True).data
        }

    return Response(dataResponse)

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes((IsAuthenticated,))
def update_profile(request : Request, slug):
    '''update profile by creator'''
    profile = Profile.objects.get(slug=slug)
    user=request.user
    if profile.user != user:
        return Response({'response':"You Don't Have Permission To Edit That"})
    updated_profile = ProfileSerializer(instance=profile, data=request.data)
    if updated_profile.is_valid():
        updated_profile.save()
        responseData = {
            "msg" : "updated successefully"
        }

        return Response(responseData)
    else:
        print(updated_profile.errors)
        return Response({"msg" : "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_profile(request: Request, slug):
    '''Delete profile by creator'''
    profile = Profile.objects.get(slug=slug)
    user=request.user
    if profile.user != user:
        return Response({'response':"You Don't Have Permission To Delete That"})
    if request.method == 'DELETE':
       opration= profile.delete()
       data={}
    if opration:
        data['success']="Deleted Successfully"
    else:
        data['faild']="Deleted failed"
    return Response(data=data)












'''@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_post(request : Request):
    account=request.user
    new_post=Post.user=account
    if request.method == "POST":
        serializer = PostSerializer(new_post,data=request.data)
    if serializer.is_valid():
        serializer.save()
        dataResponse = {
            "msg" : "Created Post Successfully",
            "post" : serializer.data}
        return Response(dataResponse)
    else:
        print(serializer.errors)
        dataResponse = {"msg" : "couldn't create a Post"}
        return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_note(request : Request):
    notes = Note.objects.all()

    dataResponse = {
        "msg" : "List of All note",
        "students" : NoteSerializer(instance=notes, many=True).data
        }

    return Response(dataResponse)

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
def update_note(request : Request, note_id):
    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    note = Note.objects.get(id=note_id)
    
    updated_note = NoteSerializer(instance=note, data=request.data)
    if updated_note.is_valid():
        updated_note.save()
        responseData = {
            "msg" : "updated successefully"
        }

        return Response(responseData)
    else:
        print(updated_note.errors)
        return Response({"msg" : "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
def delete_note(request: Request, note_id):
    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    note = Note.objects.get(id=note_id)
    note.delete()
    return Response({"msg" : "Deleted Successfully"})'''