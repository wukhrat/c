from django.db import models
from django.utils import timezone


class User(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(verbose_name="Ism", max_length=100)
    username = models.CharField(verbose_name="Telegram username", max_length=100, null=True)
    telegram_id = models.BigIntegerField(verbose_name='Telegram ID', unique=True, default=1)
    email = models.CharField(verbose_name='Email', max_length=50, null=True)

    def __str__(self):
        return f"{self.id} - {self.telegram_id} - {self.full_name}"


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(verbose_name="Mahsulot nomi", max_length=50)
    photo = models.CharField(verbose_name="Rasm file_id", max_length=200, null=True)
    price = models.DecimalField(verbose_name="Narx", decimal_places=2, max_digits=8)
    description = models.TextField(verbose_name="Mahsulot haqida", max_length=3000, null=True)
    category_name = models.CharField(verbose_name="Kategoriya nomi", max_length=30)

    def __str__(self):
        return f"{self.id} - {self.product_name}"


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name="Narx", decimal_places=2, max_digits=20)
    quantity = models.FloatField(verbose_name="quantity")
    summa = models.DecimalField(verbose_name="summa", decimal_places=2, max_digits=20)
    date = models.DateField(verbose_name="date", default=timezone.now)
    user = models.CharField(max_length=100, null=True)
    is_debt = models.CharField(max_length=50, default=False)


class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField(verbose_name="quantity")
    price = models.DecimalField(verbose_name="Narx", decimal_places=2, max_digits=8)
    summa = models.DecimalField(verbose_name="summa", decimal_places=2, max_digits=20)
    user_id = models.BigIntegerField()


class Storage(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField(verbose_name="quantity")
    price = models.DecimalField(verbose_name="price", decimal_places=2, max_digits=20)
    summa = models.DecimalField(verbose_name="summa", decimal_places=2, max_digits=20)


class Remains(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField(verbose_name="quantity")
    price = models.DecimalField(verbose_name="price", decimal_places=20, max_digits=20)
    summa = models.DecimalField(verbose_name="summa", decimal_places=2, max_digits=20)







