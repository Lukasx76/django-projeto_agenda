from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):

    # adjusting the plural name of Category. Django by default will add a 'S' to evey Model. As a rule of thumb this works but other names the result would be a little strange (Categorys). So I am telling django the plural of the word
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.name}'

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'