from . import views
from django.urls import path 


urlpatterns = [ 
    path('', views.HomePage.as_view(), name='home'),
    path('paintings/', views.PaintingPage.as_view(), name='painting'),
    path('ink/', views.InkPage.as_view(), name='ink'),
    path('pencil/', views.PencilPage.as_view(), name='pencil'),
    path('<slug:slug>/', views.ArtDetails.as_view(),name='art_details'),
    path('like/<slug:slug>', views.ArtLike.as_view(), name='art_like')
]