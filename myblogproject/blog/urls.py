from django.urls import path
from .views import BlogPostListCreate, BlogPostRetrieveUpdateDestroy, BlogPostListView, UserRegistrationView

urlpatterns = [
    path('api/register/', UserRegistrationView.as_view(), name='user-registration'),
    path('posts/', BlogPostListCreate.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', BlogPostRetrieveUpdateDestroy.as_view(), name='post-retrieve-update-destroy'),
    path('', BlogPostListView.as_view(), name='blog-home'),  
]
