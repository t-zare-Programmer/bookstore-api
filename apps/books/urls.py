from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet,AuthorViewSet,BookViewSet

router = DefaultRouter()
router.register('categories',CategoryViewSet)
router.register('authors',AuthorViewSet)
router.register('books',BookViewSet)

urlpatterns=[
    path('',include(router.urls)),
]