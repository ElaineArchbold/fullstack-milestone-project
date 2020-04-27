from django.db import models

# Create your models here.

CATEGORY_CHOICES = (
    ('Anniversary', 'ANNIVERSARY'),
    ('Baby', 'BABY'),
    ('Christening', 'CHRISTENING'),
    ('Communion', 'COMMUNION'),
    ('Engagement', 'ENGAGEMENT'),
    ('Family', 'FAMILY'),
    ('Fathers', 'FATHERS'),
    ('Fingerprint', 'FINGERPRINT'),
    ('Mothers', 'MOTHERS'),
    ('Teacher', 'TEACHER'),
    ('Wedding', 'WEDDING'),)

class Product(models.Model):
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='baby')
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
