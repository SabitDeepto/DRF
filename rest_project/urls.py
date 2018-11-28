from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from Sign_Up import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('Manage_Merchants.urls')),
    path('signup/', views.signup, name = 'signup'),

    path('api-auth', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


]

# Change admin site title
admin.site.site_header = "TikTok Backend"
admin.site.site_title = "Django"
