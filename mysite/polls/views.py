# # blog/views.py
# # 使用基础APIView类

# from rest_framework.views import APIView
# from django.http import Http404
# from .models import Article
# from .serializers import ArticleSerializer
# from rest_framework.response import Response
# from rest_framework import generics
# from rest_framework import permissions
# from .permissions import IsOwnerOrReadOnly

# class ArticleList(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)

# class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class =ArticleSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

#TODO 使用裝飾器來API view
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.views import APIView

User = get_user_model

@api_view(['GET', 'POST'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def article_list(request,format=None):
    """
    List all articles, or create a new article.
    """
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True,)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            # Very important. Associate request.user with author
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly])
def article_detail(request, pk, format=None):
    """
    Retrieve，update or delete an article instance。"""


    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# from django.template.defaulttags import register
# from django.shortcuts import render,redirect
# from . import models
# @register.filter
# def split_slice(value, key):
#     if value:
#         delimiter,arg2 = key.split("&")
#         if delimiter in value:
#             res = value.split(delimiter)[int(arg2)]
#             return res
#         else:
#             return ""
#     else:
#         return ""

# def index(request):
    # args = {
    #     "name" :"Dsio",
    #     "age" : 28,
    #     "VIP" : "True",
    #     "dc" : {
    #         "a" : 10,
    #         "b" : 20
    #     },
    #     "loops":[1,2,3,4]
    # }
    # return render(request, './polls/index.html', args)
    
    # if request.method == "POST":
    #     name = request.POST.get('name',None)
    #     age = request.POST.get('age',None)
    #     print(name,age)
    #     obj = TB_1.objects.create(name=name,age=age,candy_or_cookie="1")
    #     obj.save()
    # user_data = TB_1.objects.get(name="陳佳宏")
    # print(user_data)
    
    # request.session["isLogin"] = False
    # return render(request, './polls/index.html',{"user_data":user_data})
    # return render(request, './polls/index.html', {"date":"2022/5/10"})
# Create your views here.
# def login(request):
#     tb1_object = None  # 初始化为 None，以防异常发生
#     if request.method == "POST":
#         username = request.POST.get("name")
#         try:
#             tb1_object = TB_1.objects.get(username=username)
#             request.session["isLogin"] = True
#         except TB_1.DoesNotExist:
#             # 处理用户不存在的情况
#             print("error")
#     return render(request, './polls/index.html',{"user_data":tb1_object})

# def login(request):
#     if request.session.get("loginFlag",None):
#         return redirect("/")
#     if request.method == "POST":
#         email = request.POST.get("email",None)
#         pwd = request.POST.get("password",None)
#         if email and pwd:
#             user = models.User.objects.filter(email=email)
#             if user:
#                 _pwd = user[0].pwd
#             else:
#                 return render(request, './polls/login.html')
#             if pwd == _pwd:
#                 request.session["loginFlag"] = True
#                 request.session["username"] = user[0].name
#                 return redirect("/")
#             else:
#                 message = "密碼輸入錯誤"
#                 return render(request, './polls/login.html',{"message":message})
#     return render(request, './polls/login.html')
# def logout(request):
#     if request.session.get("loginFlag",None):
#         request.session.flush()
#         return redirect("/login/")            
#     return redirect("/")

# def register(request):
#     if request.method == "POST":
#         email = request.POST.get("email",None)
#         name = request.POST.get("name",None)
#         pwd1 = request.POST.get("password1",None)
#         pwd2 = request.POST.get("password2",None)
#         if pwd1 == pwd2:
#             user = models.User.objects.filter(email=email)
#             if user:
#                 print("帳戶已經被註冊。請重新註冊")
#                 return redirect("/register/")
#             else:
#                 new_user = models.User.objects.create(email=email,name=name,pwd=pwd1)
#                 new_user.save()
#             return redirect("/login/")
#     return render(request, './polls/register.html')
