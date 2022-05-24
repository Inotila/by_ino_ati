from . import views
from django.urls import path 


urlpatterns = [ 
    path('', views.HomePage.as_view(), name='home'),
    path('templates/paintings.html', views.PaintingPage.as_view(), name='painting'),
    path('templates/ink.html', views.InkPage.as_view(), name='ink'),
    path('templates/pencil.html', views.PencilPage.as_view(), name='pencil'),
    path('<slug:slug>/', views.ArtDetails.as_view(),name='art_details'),
    path('like/<slug:slug>', views.ArtLike.as_view(), name='art_like')
]