from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Restaurant(models.Model):
    name = models.TextField()
    address = models.TextField(blank=True, default='')
    telephone = models.TextField(blank=True, default='')
    url = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reversed('myrestaurants:restaurant_detail', args=[str(self.id)])


class Dish(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True, default='')
    price = models.DecimalField('USD amount', max_digits=8, decimal_places=2, blank=True, null=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)  # 和用户表级联
    date = models.DateTimeField(default=datetime.now())
    image = models.ImageField(upload_to="myrestaurants", blank=True,
                              null=True)  # upload_to="myrestaurants"是指定之后图片上传的路径/media/myrestaurants/文件名
    restaurant = models.ForeignKey(Restaurant, null=True, related_name='dishes', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reversed('myrestaurants:dish_detail', args=[str(self.restaurant.id), str(self.id)])


# 下面这个抽象的review类可以之后用来创建RestaurantReview 和 DishReview,作为他们的父类，所以设置为抽象

class Review(models.Model):
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))  # 选择等级
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now())

    class Meta:
        abstract = True


class RestaurantReview(Review):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return "{} review".format(self.restaurant.name)
