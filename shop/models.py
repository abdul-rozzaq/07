from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Phone(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='phones')
    phone_number = models.CharField(max_length=20)
    is_primary = models.BooleanField(default=False)
    image = models.ImageField(upload_to='phone_images/', blank=True, null=True)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    operating_system = models.CharField(max_length=50, blank=True, null=True)
    storage = models.PositiveIntegerField()
    ram = models.PositiveIntegerField()
    color = models.CharField(max_length=30, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    release_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.phone_number})"
