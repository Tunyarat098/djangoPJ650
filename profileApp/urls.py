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
    path('showOurProduct', views.showOurProduct, name="showOurProduct"),
    path('newProduct', views.newProduct, name='newProduct'),
    path('frmProduct', views.frmProduct, name='frmProduct'),

    path('listProduct', views.listProduct, name='listProduct'),
    path('inputProduct', views.inputProduct, name='inputProduct'),

    path('retrieveAllProduct', views.retrieveAllProduct, name='retrieveAllProduct'),

    path('<pid>/retrieveOneProduct', views.retrieveOneProduct, name='retrieveOneProduct'), #เอาpidไว้หน้าหรือหลังก็ได้

    path('createProduct', views.createProduct, name='createProduct'),
    path('updateProduct/<pid>',views.updateProduct, name='updateProduct'),
    path('deleteProduct/<pid>',views.deleteProduct, name='deleteProduct'),

    path('empCreate', views.empCreate, name='empCreate'),
]
