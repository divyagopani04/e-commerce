"""
URL configuration for ecom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from firstapp.views import registeruser
from firstapp.views import loginuser
from firstapp.views import logoutuser
from firstapp.views import index
from firstapp.views import about
from firstapp.views import blogdetails
from firstapp.views import bloggrid
from firstapp.views import blog
from firstapp.views import cartgrocery
from firstapp.views import addcart
from firstapp.views import viewcart
from firstapp.views import remove_cart_item
from firstapp.views import header
from firstapp.views import checkoutgrocery
from firstapp.views import checkoutpharmacy
from firstapp.views import checkout
from firstapp.views import comingsoon
from firstapp.views import contact
from firstapp.views import error
from firstapp.views import faq
from firstapp.views import grocerydetails
from firstapp.views import groceryproduct
from firstapp.views import grocery
from firstapp.views import pharmacydetails
from firstapp.views import pharmacyproduct
from firstapp.views import pharmacy
from firstapp.views import portfoliodetails
from firstapp.views import portfolio
from firstapp.views import productdetails 
from firstapp.views import product
from firstapp.views import store
from firstapp.views import wishlistgrocery
from firstapp.views import wishlistpharmacy
from firstapp.views import wishlist
from firstapp.views import myprofile
from firstapp.views import orderlist
from firstapp.views import delete_orderlist
from firstapp.views import update_quantity



#backend

from backend.views import dashboard
from backend.views import register
from backend.views import login
from backend.views import logout
from backend.views import update
from backend.views import delete
from backend.views import viewdata
from backend.views import addcategory
from backend.views import viewcategory
from backend.views import deletecategory
from backend.views import updatecategory
from backend.views import change
from backend.views import addsubcate
from backend.views import viewsubcate
from backend.views import deletesubcate
from backend.views import updatesubcate
from backend.views import subcatechange
from backend.views import addproduct
from backend.views import viewproduct
from backend.views import deleteproduct
from backend.views import updateproduct,allreguser
from backend.views import pchange

from backend import views
from firstapp import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('userregister/',registeruser),
    path('loginuser/',loginuser),
    path('logoutuser/',logoutuser),
    path('',index),
    path('about/',about),
    path('blogdetails/',blogdetails),
    path('bloggrid/',bloggrid),
    path('blog/',blog),
    path('cartgrocery/',cartgrocery),
    path('cart/<int:id>/',addcart),
    path('remove/<int:id>/',remove_cart_item),
    path('viewcart/',viewcart),
    path('header/',header),
    path('checkoutgrocery/',checkoutgrocery),
    path('checkoutpharmacy/',checkoutpharmacy),
    path('checkout/',checkout),
    path('comingsoon/',comingsoon),
    path('contact/',contact),
    path('error/',error),
    path('faq/',faq),
    path('grocerydetails/',grocerydetails),
    path('groceryproduct/',groceryproduct),
    path('grocery/',grocery),
    path('pharmacydetails/',pharmacydetails),
    path('pharmacyproduct/',pharmacyproduct),
    path('pharmacy/',pharmacy),
    path('portfoliodetails/',portfoliodetails),
    path('portfolio/',portfolio),
    path('productdetails/<int:id>',productdetails),
    path('product/',product),
    path('store/',store),
    path('wishlistgrocery/',wishlistgrocery),
    path('wishlistpharmacy/',wishlistpharmacy),
    path('wishlist/',wishlist),
    path('myprofile/',myprofile),
    path('orderlist/',orderlist),
    path('delete_orderlist/<int:id>',delete_orderlist),


      #backend

    path('dashboard/',dashboard),
    path('register/',register),
    path('login/',login),
    path('logout/',logout),
    path('update/<int:id>/',update),
    path('delete/<int:id>/',delete),
    path('viewdata/',viewdata),
    path('addcategory/',addcategory),
    path('viewcategory/',viewcategory),
    path('deletecate/<int:id>',deletecategory),
    path('updatecate/<int:id>',updatecategory),
    path('changestatus/<int:id>',change),
    path('addsubcate/',addsubcate),
    path('viewsubcate/',viewsubcate),
    path('deletesub/<int:id>',deletesubcate),
    path('updatesub/<int:id>',updatesubcate),
    path('subcatechange/<int:id>',subcatechange),
    path('addproduct/',addproduct),
    path('viewproduct/',viewproduct),
    path('updateproduct/<int:id>',updateproduct),
    path('deleteproduct/<int:id>',deleteproduct),
    path('pchange/<int:id>',pchange),
    path('allreguser/',allreguser),

    path('update_quantity/', update_quantity, name='update_quantity'),

    path('payment',views.homepage,name='payment'),
    path('paymenthandler/',views.paymenthandler,name='paymenthandler'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

