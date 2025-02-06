from django.db import models
from django.utils.translation import gettext_lazy as _



# category model

class Category (models.Model):

    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'

# brand model

class BrandStatus(models.TextChoices):

    PUBLISHED = 'PUBLISHED', _('PUBLISHED')
    DRAFT = 'DRAFT', _('DRAFT')
    PENDING = 'PENDING', _('PENDING')

class Brand(models.Model):

    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=255)

    image_path = models.ImageField(upload_to='brand', null=True, blank=True, default='No_image_available.jpg')

    status = models.CharField(
        max_length=255,
        choices=BrandStatus.choices,
        default=BrandStatus.PUBLISHED
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'brand'

# product model

class Product(models.Model):

    id = models.BigAutoField(primary_key= True)

    name = models.CharField(max_length=255)

    image_path = models.ImageField(upload_to='product', null=True, blank=True, default='No_image_available.jpg' )

    description =models.TextField(null=True)

    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    brand = models.ForeignKey(Brand, null=True, blank=True, on_delete=models.SET_NULL)

    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    qty = models.IntegerField(null=True, blank=True)

    alert_stock = models.IntegerField(null=True, blank=True)

    image_path = models.ImageField(upload_to='product', null=True, blank=True, default='no-image-available.jpg')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product'

# cart modal

class Cart(models.Model):

    id = models.BigAutoField(primary_key=True)

    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)

    qty = models.IntegerField(default=0)

    def __int__(self):
        return self.product

# order model

class OrderStatus(models.TextChoices):
    PENDING = 'PENDING',_('Pending')
    APPROVED = 'APPROVED',_('Approved')
    REJECTED = 'REJECTED',_('Rejected')

class PaymentMethod(models.TextChoices):
    CASH = 'CASH',_('CASH')
    UPI = 'UPI',_('UPI')
    CARD = 'CARD',_('CARD')

class Order(models.Model):
    id=models.BigAutoField(primary_key=True)
    order_number = models.CharField(max_length=255,blank=True,null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    order_status = models.CharField(
        max_length=255,
        choices=OrderStatus.choices,
        default=OrderStatus.PENDING
    )
    payment_method = models.CharField(
        max_length=255,
        choices=PaymentMethod.choices,
        default=PaymentMethod.CASH
    )

    class Meta:
        db_table = 'order'

# orderitem model

class OrderItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    qty = models.IntegerField(null=True,blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount = models.IntegerField(blank=True,null=True,default=0)

    def calculate_total_amount(self):
        if self.price and self.qty:
            subtotal = self.price * self.qty
            if self.discount > 0:
                discount_amount = (subtotal * self.discount) / 100
                total_amount = subtotal - discount_amount
            else:
                total_amount = subtotal
            return total_amount
        return 0

    def save(self, *args, **kwargs):
        # Automatically update amount based on the calculated total amount
        self.amount = self.calculate_total_amount()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'order_items'