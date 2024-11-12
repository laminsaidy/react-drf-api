from django.contrib import admin
from django.urls import path, include
from .views import root_route, logout_route, custom_login, YourDataView

urlpatterns = [
    path('', root_route),  
    path('login/', custom_login),  
    path('logout/', logout_route),  
    path('dj-rest-auth/', include('dj_rest_auth.urls')),  
    path('yourdata/', YourDataView.as_view(), name='yourdata'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),  
    path('profiles/', include('profiles.urls')),  
    path('posts/', include('posts.urls')),  
    path('comments/', include('comments.urls')),  
    path('likes/', include('likes.urls')),  
    path('followers/', include('followers.urls')),  
]