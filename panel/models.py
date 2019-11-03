from django.db import models
from django.urls import reverse
from datetime import timedelta, datetime, timezone
# Create your models here.


class Client(models.Model):
    email = models.EmailField(max_length=200)
    reg_date = models.DateTimeField('register date')

    def __str__(self):
        return self.email


class Game(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class LicenseKey(models.Model):
    created_date = models.DateTimeField('created date')
    expire_date = models.DateTimeField('expire date')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, blank=True, null=True)

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
        return '{} - {}'.format(self.game, self.client)


class Post(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField()
    pub_date = models.DateTimeField()
    slug = models.SlugField(max_length=250, unique_for_date='pub_date')

    def __str__(self):
            return self.title

    def get_absolute_url(self):
        return reverse('panel:post_detail', args=[self.pub_date.year, self.pub_date.month,
                                                    self.pub_date.day, self.slug])