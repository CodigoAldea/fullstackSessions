from django.db import models



class expense(models.Model):
    
    CATEGORY_CHOICES= [
        # value , display value
        ('Food', 'Food'),
        ('Travel', 'Travel'),
        ('Others', 'Others')
    ]
    
    category = models.CharField(max_length=100, choices= CATEGORY_CHOICES)
    description = models.CharField(max_length=500)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date= models.DateField(auto_now_add= True)