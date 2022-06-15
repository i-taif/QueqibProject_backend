from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import City,Profile,Post,Comment
from .serializers import CitySerializer,PostSerializer,ProfileSerializer, CommentSerializer, ViweUserSerializer, ViweAllUserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def list_user_info(request : Request,id):
    '''list  user ifo'''
    user = User.objects.filter(id=id)
    dataResponse = {
        "msg" : "List user info ",
        "user" : ViweUserSerializer(instance=user, many=True).data
        }
    return Response(dataResponse)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def list_all_user(request : Request):
    '''list all user '''
    user = User.objects.all()
    dataResponse = {
        "msg" : "List all user  ",
        "user" : ViweAllUserSerializer(instance=user, many=True).data
        }
    return Response(dataResponse)

@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_user(request: Request, id):
    '''Delete user by editors'''
    account = User.objects.get(id=id)
    user=request.user
    if  not user.has_perm('auth.delete_user'):
        return Response({'msg':"You Don't Have Permission To Delete That"})
    account.delete()
    return Response({"msg" : "Deleted Successfully"})



@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_city(request : Request):
    ''' add city by editors'''
    account= request.user
    if not account.is_authenticated or not account.has_perm('QueqibApp.add_city'):
        return Response("You Don't Have Permission To add That", status = status.HTTP_400_BAD_REQUEST)
    request.data["user"] = request.user.id
    serializer = CitySerializer(data=request.data)
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
        return Response("You Don't Have Permission To Edit That", status = status.HTTP_400_BAD_REQUEST)
    city = City.objects.get(slug=slug)
    request.data["user"] = request.user.id
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
def list_cities(request : Request):
    '''list all city'''
    cities = City.objects.all()

    dataResponse = {
        "msg" : "List of All cities",
        "cities" : CitySerializer(instance=cities, many=True).data
        }

    return Response(dataResponse)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def city_details(request : Request,id):
    '''city details'''
    city = City.objects.get(id=id)

    dataResponse = {
        "msg" : "The city Details",
        "city" : CitySerializer(instance=city).data
        }

    return Response(dataResponse)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def search_city(request : Request,name):
    '''search city'''
    cities = City.objects.filter(City_name__contains=name)

    dataResponse = {
        "msg" : "List of search",
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
        return Response("You Don't Have Permission To Delete That", status = status.HTTP_400_BAD_REQUEST)
    city = City.objects.get(slug=slug)
    city.delete()
    return Response({"msg" : "Deleted Successfully"})


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_profile(request : Request):
    ''' create profile by Tour guide'''
    user= request.user
    if not user.is_authenticated or not user.has_perm('QueqibApp.add_profile'):
        return Response("You Don't Have Permission to Create Profile", status = status.HTTP_400_BAD_REQUEST)
    request.data["user"] = request.user.id
    serializer = ProfileSerializer(data=request.data)
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
def list_all_profile(request : Request):
    '''list all profile'''
    profiles = Profile.objects.all()

    dataResponse = {
        "msg" : "List of All profiles",
        "profile" : ProfileSerializer(instance=profiles, many=True).data
        }

    return Response(dataResponse)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def profile_details(request : Request,user_id):
    '''profile details'''
    profile = Profile.objects.get(user_id=user_id)

    dataResponse = {
        "msg" : "The profile Details",
        "profile" : ProfileSerializer(instance=profile).data
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
    request.data["user"] = request.user.id
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


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_post(request : Request):
    ''' add post by tour guide'''
    user= request.user
    if not user.is_authenticated or not user.has_perm('QueqibApp.add_post'):
        return Response("You Don't Have Permission To add That", status = status.HTTP_400_BAD_REQUEST)

    request.data["profile"] = Profile.objects.get(user=request.user.id).user
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        dataResponse = {
            "msg" : "Created post Successfully",
            "post" : serializer.data}
        return Response(dataResponse)
    else:
        print(serializer.errors)
        dataResponse = {"msg" : "couldn't create a post"}
        return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def list_post(request : Request):
    '''list all post'''
    posts = Post.objects.all()
    dataResponse = {
        "msg" : "List of All posts",
        "posts" : PostSerializer(instance=posts, many=True).data
        }
    return Response(dataResponse)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def post_details(request : Request,slug):
    '''post details'''
    post = Post.objects.get(slug=slug)

    dataResponse = {
        "msg" : "The Post Details",
        "post" : PostSerializer(instance=post).data
        }

    return Response(dataResponse)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes((IsAuthenticated,))
def update_post(request : Request, slug):
    '''update profile by creator'''
    post = Post.objects.get(slug=slug)
    user=request.user
    if post.profile.user != user:
        return Response({'msg':"You Don't Have Permission To Edit That"})
    request.data["profile"] = Profile.objects.get(user=request.user.id).user
    updated_post = PostSerializer(instance=post, data=request.data)
    if updated_post.is_valid():
        updated_post.save()
        responseData = {
            "msg" : "updated successefully"
        }

        return Response(responseData)
    else:
        print(updated_post.errors)
        return Response({"msg" : "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_post(request: Request, slug):
    '''Delete post by creator and editors'''
    post = Post.objects.get(slug=slug)
    user=request.user
    if post.profile.user != user and not user.has_perm('QueqibApp.delete_post'):
        return Response({'msg':"You Don't Have Permission To Delete That"})
    post.delete()
    return Response({"msg" : "Deleted Successfully"})


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_comment(request : Request):
    ''' add comment by all users'''
    user= request.user
    if not user.is_authenticated:
        return Response("You Can't add comment", status = status.HTTP_400_BAD_REQUEST)
    request.data["user"] = request.user.id
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        dataResponse = {
            "msg" : "add comment Successfully",
            "comment" : serializer.data}
        return Response(dataResponse)
    else:
        print(serializer.errors)
        dataResponse = {"msg" : "couldn't add a comment"}
        return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def list_comments(request : Request,post_id):
    '''list all comments'''
    comments = Comment.objects.filter(post_id=post_id)
    dataResponse = {
        "msg" : "List of All comments",
        "comments" : CommentSerializer(instance=comments, many=True).data
        }
    return Response(dataResponse)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def list_all_comments(request : Request):
    '''list all comments'''
    comments = Comment.objects.all()
    dataResponse = {
        "msg" : "List of All comments",
        "comments" : CommentSerializer(instance=comments, many=True).data
        }
    return Response(dataResponse)

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes((IsAuthenticated,))
def update_comment(request : Request, slug):
    '''update comment by creator'''
    comment = Comment.objects.get(slug=slug)
    user=request.user
    if comment.user != user:
        return Response({'response':"You Don't Have Permission To Edit That"})
    request.data["user"] = request.user.id
    updated_comment = CommentSerializer(instance=comment, data=request.data)
    if updated_comment.is_valid():
        updated_comment.save()
        responseData = {
            "msg" : "updated successefully"
        }

        return Response(responseData)
    else:
        print(updated_comment.errors)
        return Response({"msg" : "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_comment(request: Request, slug):
    '''Delete comment by creator and editors'''
    comment = Comment.objects.get(slug=slug)
    user=request.user
    if comment.user != user and not user.has_perm('QueqibApp.delete_comment'):
        return Response({'response':"You Don't Have Permission To Delete That"})
    comment.delete()
    return Response({"msg" : "Deleted Successfully"})
