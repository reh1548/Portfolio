from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('blog_single/<int:id>/', views.blog_single, name='blog_single'),
    path('add_comment/<int:blog_id>/', views.add_comment, name='add_comment'),
]
