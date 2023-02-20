from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import index,endpoints
from . import views

urlpatterns = [
    path('' ,views.endpoints),
    path('advocates/',views.advocates_list),
    path('advocates/<int:id>',views.advocates_detail),
    path('advocates/add',views.add_advocate),
]
