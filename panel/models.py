from django.db import models
from datetime import timedelta, datetime, timezone
# Create your models here.


class Client(models.Model):
    email = models.EmailField(max_length=200)
    reg_date = models.DateTimeField('register date')

    def __str__(self):
        return self.email


class Product(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class LicenseKey(models.Model):
    created_date = models.DateTimeField('created date')
    expire_date = models.DateTimeField('expire date')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)

    def time_left(self):     
        today = datetime.now(timezone.utc) 
        if self.expire_date > today:
            left = self.expire_date - today          
            return '{} days, {} hours'.format(left.days, left.seconds // 3600)
        else:
            return 'expired'

    def add_days(self, amount):
        self.expire_date = self.expire_date + timedelta(days=amount)
    
    def __str__(self):
        return '{} - {}'.format(self.product, self.client)


class NewsPost(models.Model):
    title = models.CharField(max_length=300)
    post_text = models.TextField()
    pub_date = models.DateTimeField()

    def __str__(self):
            return self.title