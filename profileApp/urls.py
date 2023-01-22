from django.urls import path
from profileApp import views

urlpatterns = [
    path('profile', views.profile, name="profile"),
    path('edu', views.edu, name="edu"),
    path('interest', views.interest, name="interest"),
    path('influ', views.influ, name="influ"),
    path('product', views.product, name="product"),
    path('test', views.test, name="test"),
    path('showMydataGroup', views.showMydataGroup, name='showMydataGroup'),
    path('showMyData', views.showMyData, name="showMyData"),
]
