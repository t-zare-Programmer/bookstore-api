from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name
#_________________________________________________________________________________
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = 'Authors'
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
#_________________________________________________________________________________
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,related_name='books')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True,related_name='books')
    description = models.TextField()
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveSmallIntegerField(default=0)
    cover_image = models.ImageField(upload_to='book_covers/',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = 'Books'
        ordering = ['title']

    def __str__(self):
        return self.title

