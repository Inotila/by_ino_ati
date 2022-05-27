from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('art/', views.art_views, name='art_views'),
    path('<slug:slug>/', views.ArtDetails.as_view(), name='art_details'),
    path('like/<slug:slug>', views.ArtLike.as_view(), name='art_like')
    ]
