"""url imports"""
from django.urls import path
from art.views import edit_comment, delete_comment
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    # path('', views.HomePage.as_view(), name='home'),
    path('art/', views.art_views, name='art_views'),
    path('<slug:slug>/', views.ArtDetails.as_view(), name='art_details'),
    path('like/<slug:slug>', views.ArtLike.as_view(), name='art_like'),
    path('edit/<comment_id>', edit_comment, name='edit'),
    path('delete/<comment_id>', delete_comment, name='delete'),
    ]
