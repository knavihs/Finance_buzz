from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.registration,name='registration'),
    path('login/',views.login_site,name='login_site'),
    path('login/submission/', views.login_action, name='login_action'),
    path('logout/',views.logout_site,name='logout_site'),
    path('addstock/<str:user>',views.add_stock,name ='add_stock'),
    path('download/<str:company>',views.downloadable,name='downloadable')
    ]