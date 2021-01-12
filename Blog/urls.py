from django.urls import path
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import BlogsAddAPIView,BlogsAPIView, BlogRetrieveAPIView, BlogDestroyAPIView

urlpatterns = [
    path('api/add_blog/', BlogsAddAPIView.as_view()),
    path('api/blogs_list/', BlogsAPIView.as_view()),
    path('api/blogs/details/<int:pk>/', BlogRetrieveAPIView.as_view()),
    path('api/blogs/delete/<int:pk>/', BlogDestroyAPIView.as_view()),
]
