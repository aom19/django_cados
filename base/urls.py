from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views


urlpatterns = [
    path('' ,views.endpoints),
    path('advocates/',views.AdvocatesList.as_view() , name = 'advocates-list'),
    path('advocates/<int:id>',views.AdvocateDetail.as_view()),
    path('companies/',views.CompanyList.as_view() , name = 'companies-list'),

]
