from django.db import models
from django.utils import timezone


class User(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=256)

    def __str__(self):
        return '%s' % (self.username)


class List(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    date_created = models.DateTimeField(default=timezone.now())

    def get_item_count(self):
        item_count = len(Item.objects.filter(list=self))
        return item_count

    def __str__(self):
        return '%s' % (self.name)


class Item(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    primary = models.CharField(max_length=256)
    secondary = models.CharField(max_length=256)
    comments = models.CharField(max_length=256, blank=True)
    occur = models.IntegerField(default=0)
    correct = models.IntegerField(default=0)
    incorrect = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=timezone.now())

    def marks_total(self):
        return self.correct + self.incorrect

    def marks_percent(self):
        if self.marks_total() > 0:
            return round((self.correct / self.marks_total()) * 100)
        else:
            return 0

    def __str__(self):
        return '%s' % (self.primary)
