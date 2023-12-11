from rest_framework import serializers
from .models import Article
from django.contrib.auth import get_user_model

User = get_user_model()

# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=True, allow_blank=True, max_length=90)
#     body = serializers.CharField(required=False, allow_blank=True)
#     author = serializers.ReadOnlyField(source="author.id")
#     status = serializers.ChoiceField(choices=Article.STATUS_CHOICES, default='p')
#     create_date = serializers.DateTimeField(read_only=True)

#     def create(self, validated_data):
#         """
#         Create a new "article" instance
#         """
#         return Article.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Use validated data to return an existing `Article`instance。"""
#         instance.title = validated_data.get('title', instance.title)
#         instance.body = validated_data.get('body', instance.body)
#         instance.status = validated_data.get('status', instance.status)
#         instance.save()
#         return instance
    
        # author = serializers.HiddenField(default=serializers.CurrentUserDefault())
        
# class UserSerializer(serializers.ModelSerializer):
    
#     articles = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

#     class Meta:
#         model = User
#         fields = ('id', 'username', 'articles',)
#         read_only_fields = ('id', 'username',)
        
        
class UserSerializer(serializers.ModelSerializer):
    articles = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'articles',)
        read_only_fields = ('id', 'username',)
        
#TODO 可以設定字段內容驗證        
def title_gt_90(value):
    if len(value) < 5:
        raise serializers.ValidationError('标题字符长度不低于5。')
        
            
class ArticleSerializer(serializers.ModelSerializer):
    title = serializers.CharField(validators=[title_gt_90])
    # author = serializers.ReadOnlyField(source="author.username")
    author = UserSerializer(read_only=True)
    status  = serializers.ReadOnlyField(source="get_status_display")
    cn_status = serializers.SerializerMethodField()
    create_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('id', 'author', 'create_date')
        # depth = 1
        
    # def to_representation(self, value):
    #     # 调用父类获取当前序列化数据，value代表每个对象实例ob
    #     data = super().to_representation(value)
    #     # 对序列化数据做修改，添加新的数据
    #     data['total_likes'] = value.liked_by.count()
    #     return data
    #     read_only_fields = ('id', 'author', 'create_date')
        
    def get_cn_status(self, obj):
        if obj.status == 'p':
            return "已發表"
        elif obj.status == 'd':
            return "草稿"
        else:
            return ''
    #TODO 驗證字段內容是否有含"django"
    def validate_body(self, value):
        """
        Check that the article is about Django.
        """
        if 'django' not in value.lower():
            raise serializers.ValidationError("Article is not about Django")
        return value
    #TODO 驗證多個字段
    # def validate(self, data):
    #     """
    #     Check that the start is before the stop.
    #     """
    #     if data['status'] > data['finish']:
    #         raise serializers.ValidationError("finish must occur after start")
        return data
    # TODO 反序列化     
    # def create(self, validated_data):
    #     """
    #     Create and return a new `Article` instance, given the validated data.
    #     """
    #     validated_data['created_by'] = self.context['request'].user  # 假設你有一個 'created_by' 字段

    #     return Article.objects.create(**validated_data)