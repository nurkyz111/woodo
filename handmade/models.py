from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Category')

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_detail', args=[self.id])


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='product')
    name = models.CharField(max_length=25, verbose_name='Name')
    description = models.TextField(verbose_name='description')
    image = models.ImageField(upload_to='products/', verbose_name='Image', default='default.jpg')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    made_by = models.CharField(max_length=255)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id])


class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=18)
    email = models.EmailField()
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return f'{self.name} - {self.phone_number}'


class Trends(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='products/', verbose_name='Image', default='default.jpg')

    def __str__(self):
        return f'{self.title}'


class Testimonial(models.Model):
    author = models.CharField(max_length=50)
    text = models.TextField()
    image = models.ImageField(upload_to='products/', verbose_name='Image', default='default.jpg')

    def __str__(self):
        return f'{self.author} - {self.image}'


