from django.db import models

# Create your models here.
class Products (models.Model):
    cat =[('1','category_1'),('2','category_2')]
    name = models.CharField(max_length=100,verbose_name="title")
    content = models.TextField()
    price= models.DecimalField(max_digits=6,decimal_places=2)
    image = models.ImageField(upload_to="photos/%y/%m/%d")
    active=models.BooleanField(default=True)
    category =models.CharField(blank=True,null=True,choices=cat)

    def __str__(self):
        return  self.name  ## rename display table admin dashboard

    class Meta :
        verbose_name='table'
        # ordering=['price'] # order by small
        ordering=['-price'] # order by big