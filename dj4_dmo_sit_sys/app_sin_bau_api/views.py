#TODO 使用裝飾器來API view
import base64
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate
from django.shortcuts import render


@api_view(["GET", "POST"])
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([BasicAuthentication])
def do_article_list(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True,)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            # Very important. Associate request.user with author

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(["GET", "PUT", "DELETE"])
@permission_classes([permissions.IsAuthenticated, IsOwnerOrReadOnly])
@authentication_classes([BasicAuthentication])
def do_article_detail(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# sqlite 對比
def do_verify_user(username, password):
    try:
        obj_user = User.objects.filter(username=username)

        if obj_user.count() != 1:
            return False

        print("比對數據庫用戶中~~~~")
        user = obj_user.first()
        return check_password(password, user.password)

    except User.DoesNotExist:
        return False


# 收python json 數據
@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated,IsOwnerOrReadOnly])
@authentication_classes([BasicAuthentication])
def api_python_api_text(request):
    if request.method == "POST":
        auth_header = request.META.get("HTTP_AUTHORIZATION")
        if auth_header:
            _, base64_data = auth_header.split(" ")
            decoded_data = base64.b64decode(base64_data).decode("utf-8")
            username, password = decoded_data.split(":")
            print(username, password)

            # 使用 Django 的 authenticate 驗證用戶和密码
            user = authenticate(request, username=username, password=password)
            verification_result = do_verify_user(username, password)
            if user:
                print("用戶驗證成功")

                return JsonResponse({"verification_result": verification_result})
            else:
                print("用戶驗證失敗")
                return JsonResponse({"verification_result": verification_result})
        else:
            print("未提供身分證信息")
            return JsonResponse({"verification_result": False})

