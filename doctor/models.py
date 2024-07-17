from django.db import models

# Create your models here.
class maincategory(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField( max_length=50)
    
    def __str__(self):
        return str(self.id)+ '   ---  ' +self.name
    
class medicine(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    brand=models.CharField(max_length=60)
    pic=models.ImageField(upload_to='upload',default=None,blank=True,null=True)
    price=models.IntegerField()
    discount=models.IntegerField()
    finalprice=models.IntegerField()
    quantity=models.IntegerField()
    
    total_price = models.IntegerField()

    def save(self, *args, **kwargs):
        if self.finalprice is not None and self.quantity is not None:
            self.total_price =(int (self.finalprice) * int(self.quantity))
        super().save(*args, **kwargs)
    
    def __str__(self):
        return str(self.id)+ '   ---  ' +self.name
    