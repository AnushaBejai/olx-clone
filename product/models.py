from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone 
from django.utils.text import slugify

class Product(models.Model):
    condition_type=(
        ("New","New"),
        ("Used","Used")
    )
    #contains all the product information
    name=models.CharField(max_length=100)
    owner= models.ForeignKey(User, on_delete=models.CASCADE)
    description=models.TextField(max_length=500)
    conditon=models.CharField(max_length=100, choices=condition_type)
    category= models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    brand= models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)
    price=models.DecimalField(max_digits=10, decimal_places=5)
    image=models.ImageField(upload_to='main_product/', blank=True, null=True)
    created=models.DateTimeField(default=timezone.now)
    slug=models.SlugField(blank=True, null=True)


    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug=slugify(self.name)
        super(Product, self).save( *args, **kwargs)

    def __str__(self):
        return self.name  

class ProductImages(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='products/', blank=True, null=True)

    class Meta:
        verbose_name='Product Image'
        verbose_name_plural='Product Images' #name in admin
    def __str__(self):
        return self.product.name


class Category(models.Model):
    # for product category 
    category_name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='category/', blank=True, null=True)
    slug=models.SlugField(blank=True, null=True)


    def save(self, *args, **kwargs):
        if not self.slug and self.category_name:
            self.slug=slugify(self.category_name)
        super(Category, self).save( *args, **kwargs)


    class Meta:
        verbose_name='category'
        verbose_name_plural='categories' #name in admin

    def __str__(self):
        return self.category_name

class Brand(models.Model):
    # for product brand 
    brand_name=models.CharField(max_length=50)
    
    class Meta:
        verbose_name='brand'
        verbose_name_plural='brands' #name in admin

    def __str__(self):
        return self.brand_name
