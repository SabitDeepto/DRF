from django.contrib import admin
from django.urls import path, include
# from Sign_Up import views
from rest_project import views
# from Person import views


urlpatterns = [
    # path('admin/', admin.site.urls)
    path('admin/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('ambassador/', include('Manage_Ambassador.urls')),


    path('create_hub/', views.hub, name='hub'),
    path('hub_manager/', views.hub_table, name='hub_table'),
    path('merchant/', views.merchant, name='merchant'),
    path('pickup/', views.pickup, name='pickup'),
    path('call_centre_executive/', views.call_centre_executive, name='call_centre_executive'),
    path('handle_pickup_request/', views.handle_pickup_request, name='handle_pickup_request'),

    path('fulfill_manager/', views.fulfill_manager, name='fulfill_manager'),
    path('check_order/', views.check_order, name='check_order'),

    path('admin/signup', views.signup, name='signup'),




    path('', include('Manage_Merchants.urls')),


]


# Change admin site title
admin.site.site_header = "TikTok Backend"
admin.site.site_title = "Django"
