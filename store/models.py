from django.db import models
from category.models import category  # Ensure the correct import
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    analysis = models.TextField(max_length=40, blank=False, default='No analysis available yet.')
    prediction = models.TextField(max_length=4, blank=False, default='2')
    description = models.TextField(max_length=2000, blank=True)
    image = models.ImageField(upload_to='photos/products/')
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(category, on_delete=models.CASCADE)  # Use the correct model name
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name
 