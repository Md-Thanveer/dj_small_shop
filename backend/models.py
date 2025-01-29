from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    id = models.BigAutoField(primary_key=True)

    name= models.CharField(max_length=255)

    def __str__(self):
        return self.name
    class Meta:
        db_table = "category"

class BrandStatus(models.TextChoices):
    PUBLISHED = 'PUBLISHED', _('PUBLISHED')
    DRAFT = 'DRAFT', _('DRAFT')
    PENDING = 'PENDING', _('PENDING')

class Brand(models.Model):
    id = models.BigAutoField(primary_key=True)
    name= models.CharField(max_length=255)
    image_path= models.ImageField(upload_to='brands', null=True, blank=True, default='No_image_available.jpg')
    status= models.CharField(
        max_length=255,
        choices=BrandStatus.choices,
        default=BrandStatus.PUBLISHED
    )

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'brand'

    class Product(models.Model):
        id = models.BigAutoField(primary_key=True)
        name = models.CharField(max_length=255)
        description = models.TextField(null=True, blank=True)
        category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
        brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True, blank=True)

