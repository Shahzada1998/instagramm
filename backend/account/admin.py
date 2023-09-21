# from django.contrib import admin
#
# from django.contrib.sites import requests
# from requests import Response
# from rest_framework import status
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.decorators import api_view, authentication_classes, permission_classes
#
# from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
# from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
#
# from .models import Forum, Comment
# from .permissions import Permission
# from .serializers import ForumSerializer, CommentSerializer
#
#
# class ForumListCreateApiView(ListCreateAPIView):
#     queryset = Forum.objects.all()
#     serializer_class = ForumSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     authentication_classes = [TokenAuthentication]
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
#
#
# class ForumRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
#     queryset = Forum.objects.all()
#     serializer_class = ForumSerializer
#     permission_classes = [Permission]
#     authentication_classes = [TokenAuthentication]
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
#
#
# @api_view(http_method_names=['GET', 'POST'])
# @authentication_classes(authentication_classes=[TokenAuthentication])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def forum_list_create_api_view(request):
#     if request.method == 'POST' and request.user.is_authenticated:
#         serializer = ForumSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     if request.method == 'GET':
#         tweets = Forum.objects.all()
#         serializer = ForumSerializer(data=tweets, many=True)
#         print(serializer.data)
#         return Response(serializer.data)
#
#
# class CommentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [Permission]
#     authentication_classes = [TokenAuthentication]
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


#
# from rest_framework import serializers
#
# from .models import Forum, Comment
#
#
# class ForumSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Forum
#         fields = '__all__'
#
#
# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = '__all__'
#         read_only_fields = ['user']

#
# from rest_framework.permissions import BasePermission, SAFE_METHODS
#
#
# class Permission(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method in SAFE_METHODS:
#             return True
#         if request.user and (request.user.is_authenticated or request.user.is_staff) and obj.user == request.user:
#             return True
#         return False
#
#     def has_permission(self, request, view):
#         if request.method in SAFE_METHODS:
#             return True
#         return bool(request.user and request.user.is_authenticated)

#
# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('forum/', views.ForumListCreateApiView),
#     path('news/<int:pk>/', views.ForumRetrieveUpdateDestroyApiView.as_view()),
#     path('forum/<int:pk>/comments/', views.forum_list_create_api_view),
#     path('forum/<int:pk>/comments/<int:pk>', views.CommentRetrieveUpdateDestroyAPIView.as_view()),
#
# ]
