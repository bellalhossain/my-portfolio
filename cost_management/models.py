from __future__ import unicode_literals
from django.db import models


class Expense(models.Model):
    amount = models.IntegerField()
    Bookname = models.CharField(max_length=250)
	#cost = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.purpose
class Expenseaaa(Expense):
    Price= models.IntegerField()
    Book = models.CharField(max_length=250)
	#Cost = models.IntegerField()
    #date = models.DateTimeField(auto_now_add=True)

    def new_method(self):
        return self.price
