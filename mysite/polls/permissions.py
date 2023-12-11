from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        # 讀取權限被允許用於任何請求，
        # 所以我們總是允許 GET，HEAD 或 OPTIONS 請求。
        if request.method in permissions.SAFE_METHODS:
            return True
        

        # 寫入權限只允許給文章的作者。
        return obj.author == request.user