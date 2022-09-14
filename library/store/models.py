from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    name = models.CharField(max_length = 200,default='')
    author = models.CharField(max_length = 100,default='')
    mrp = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f'{self.name} by {self.author}'

class Librarian(models.Model):
    User = models.CharField(max_length=100)
    Library = models.CharField(max_length=100)
    Book = models.CharField(max_length=100)
    Librarian = models.CharField(max_length=100)

    def __str__(self):
        return self.User
class BookReturn(models.Model):
    books=models.ManyToManyField(Book)
    customer=models.ForeignKey(User,related_name='customer',null=True,on_delete=models.SET_NULL)
    
    
    def __str__(self):
        return(self.customer.username)



