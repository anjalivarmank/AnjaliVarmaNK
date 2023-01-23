from django.urls import path
from Stellarfront import views

urlpatterns=[
    path('index1/',views.index1,name='index1'),
    path('aboutpg/',views.aboutpg,name='aboutpg'),
    path('contactpg/',views.contactpg,name='contactpg'),
    path('productpg/',views.productpg,name='productpg'),
    path('discategory/<itemcatg>', views.discategory, name="discategory"),
    path('prodetails/<int:dataid>/',views.prodetails,name='prodetails'),
    path('messagefun/',views.messagefun,name='messagefun')

]
