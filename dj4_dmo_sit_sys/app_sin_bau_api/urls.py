from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path("articles/", views.do_article_list),
    path("articles/<int:pk>", views.do_article_detail, name="article-detail"),  # 這也是表示 正規表示法的方法

    # re_path(r"^articles/(?P<pk>[0-9]+)$", views.do_article_detail, name="article-detail"),
    # 正規表示法 之前是用在url 現在url 被re_path 取代。
    # path(r"^articles/$", views.ArticleList.as_view()),
    # path(r"^articles/(?P<pk>[0-9]+)$", views.ArticleDetail.as_view()),
    path("go_api_python_api_text/", views.api_python_api_text)
]
# urlpatterns = format_suffix_patterns(urlpatterns)
