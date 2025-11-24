from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly,AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import CategorySerializer, AuthorSerializer, BookSerializer
from rest_framework import viewsets
from .models import Book,Category,Author


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.select_related('author', 'category').all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # اضافه کردن فیلترها
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # فلتر پیشرفته
    filterset_fields = ['category', 'author']

    # سرچ روی چند فیلد
    search_fields = ['title', 'description', 'author__name']

    # مرتب‌سازی
    ordering_fields = ['price', 'title']
    ordering = ['title']
