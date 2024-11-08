from django.contrib import admin
from django.urls import path, include
from .views import root_route, logout_route, custom_login, YourDataView

urlpatterns = [
    path('', root_route),  # Root route
    path('login/', custom_login),  # Custom login
    path('logout/', logout_route),  # Custom logout
    path('api/auth/', include('dj_rest_auth.urls')),  # Default auth routes
    path('yourdata/', YourDataView.as_view(), name='yourdata'),
    path('admin/', admin.site.urls),  # Admin
    path('api-auth/', include('rest_framework.urls')),  # DRF auth
    path('dj-rest-auth/', include('dj_rest_auth.urls')),  # dj-rest-auth
    path('', include('profiles.urls')),  # Include profiles URLs
    path('', include('posts.urls')),  # Include posts URLs
    path('', include('comments.urls')),  # Include comments URLs
    path('', include('likes.urls')),  # Include likes URLs
    path('', include('followers.urls')),  # Include followers URLs
]