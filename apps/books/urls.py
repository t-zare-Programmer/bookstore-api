from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, CategoryViewSet, AuthorViewSet

router = DefaultRouter()
router.register('books', BookViewSet, basename='books')
router.register('categories', CategoryViewSet, basename='categories')
router.register('authors', AuthorViewSet, basename='authors')

urlpatterns = router.urls