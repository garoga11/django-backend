from django.contrib import admin
from django.urls import path, include

# static files config
from django.conf import settings
from django.conf.urls.static import static

from users.views import users as users_views
from users.views.login import UserLoginAPIView as login
from posts.views import PostsViewSet

# from Django REST framework
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', PostsViewSet, basename='posts')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', users_views.UserListView.as_view(), name='users'),
    path('users/login/', login.as_view(), name='login'),
    path('users/signup/', users_views.signup, name='signup'),
    path('users/verified/', users_views.account_verification, name='verified'),
    path('', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
