from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

# class Article(models.Model):
#     title = models.CharField(max_length=256)
#     body = models.TextField()
#     liked_by = models.ManyToManyField(to=User)
    
#     def __str__(self):
#         return self.title

User = get_user_model()


class Article(models.Model):
    """Article Model"""
    STATUS_CHOICES = (
        ('p', _('Published')),
        ('d', _('Draft')),
    )

    title = models.CharField(verbose_name=_('Title (*)'), max_length=90, db_index=True)
    body = models.TextField(verbose_name=_('Body'), blank=True)
    author = models.ForeignKey(User, verbose_name=_('Author'), on_delete=models.CASCADE, related_name='articles')
    status = models.CharField(_('Status (*)'), max_length=1, choices=STATUS_CHOICES, default='p', null=True, blank=True)
    create_date = models.DateTimeField(verbose_name=_('Create Date'), auto_now_add=True)
    # created_by = models.TextField(verbose_name=_('created_by'), blank=True)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_date']
        verbose_name = "Article"
        verbose_name_plural = "Articles"

# class User(models.Model):
#     email = models.EmailField(unique=True)
#     name = models.CharField(max_length=64)
#     pwd = models.CharField(max_length=64)
#     _time = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.email
    
#     class Meta:
#         ordering = ["-_time"]
#         verbose_name = "用戶資料庫"
#         verbose_name_plural = "用戶資料庫"
# class TB_1(models.Model):
    
#     NAME_CHOICES = [
#         ("0","Dio"),
#         ("1","Admin"),
#         ("2","陳佳宏")
#     ]
    
#     name = models.CharField(
#         max_length=64,
#         #choices= NAME_CHOICES,
#     )
#     age = models.IntegerField()
    
#     MY_CHOICES = [
#         ('0','糖果'),
#         ('1','餅乾'),
#     ]
    
#     candy_or_cookie = models.CharField(
#         max_length= 1,
#         choices= MY_CHOICES,
#         default= '0',
#     )
    
#     _time = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.name
    
#     class Meta:
#         ordering = ['-_time']
#         verbose_name = "用戶資料庫"
#         verbose_name_plural = "用戶資料庫"