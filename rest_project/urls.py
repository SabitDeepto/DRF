from django.contrib import admin
from django.urls import path, include
# from Sign_Up import views
from rest_project import views


urlpatterns = [

    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', views.login, name='login'),
    path('admin/signup', views.signup, name='signup'),
    path('admin/index', views.index, name='index'),



    path('', include('Manage_Merchants.urls')),


]


# Change admin site title
admin.site.site_header = "TikTok Backend"
admin.site.site_title = "Django"
