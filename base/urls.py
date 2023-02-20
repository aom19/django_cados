from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('' ,views.endpoints),
    path('advocates/',views.advocates_list , name = 'advocates-list'),
    path('advocates/<int:id>',views.advocates_detail),

]
