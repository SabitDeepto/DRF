from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

# from Sign_Up import views
from rest_project import views, settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [

    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', views.login, name='login'),
    path('admin/signup', views.signup, name='signup'),
    path('admin/index', views.index, name='index'),



    path('', include('Manage_Merchants.urls')),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+staticfiles_urlpatterns()


# Change admin site title
admin.site.site_header = "TikTok Backend"
admin.site.site_title = "Django"
