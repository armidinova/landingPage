from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    short_description = models.TextField(blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    image = models.ImageField(upload_to='products_images/', default='products_images/def.jpg')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


