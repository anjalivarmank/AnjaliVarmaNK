from django.urls import path
from StellarApp import views


urlpatterns=[
    path('indexpg/',views.indexpg,name='indexpg'),
    path('adminpg/',views.adminpg,name='adminpg'),
    path('admindb_fun/',views.admindb_fun,name='admindb_fun'),
    path('displayadminpg/',views.displayadminpg,name='displayadminpg'),
    path('editadmin/<int:dataid>',views.editadmin,name='editadmin'),
    path('updateadmin/<int:dataid>',views.updateadmin,name='updateadmin'),
    path('deleteadmin/<int:dataid>',views.deleteadmin,name='deleteadmin'),

    path('categorypg/',views.categorypg,name='categorypg'),
    path('categorydb_fun/',views.categorydb_fun,name='categorydb_fun'),
    path('displaycategorypd/',views.displaycategorypd,name='displaycategorypd'),
    path('editcategory/<int:dataid>', views.editcategory, name='editcategory'),
    path('updatecategory/<int:dataid>', views.updatecategory, name='updatecategory'),
    path('deletecategory/<int:dataid>', views.deletecategory, name='deletecategory'),

    path('addproductspg/',views.addproductspg,name='addproductspg'),
    path('addproductdb_fun/',views.addproductdb_fun,name='addproductdb_fun'),
    path('displayproduct/',views.displayproduct,name='displayproduct'),
    path('editproduct/<int:dataid>',views.editproduct,name='editproduct'),
    path('updateproduct/<int:dataid>',views.updateproduct,name='updateproduct'),

    path('logindata/',views.logindata,name='logindata'),
    path('logindb_fun/',views.logindb_fun,name='logindb_fun'),

    path('logout_fun/',views.logout_fun,name='logout_fun'),

    path('messagefu/',views.messagefu,name='messagefu')



]