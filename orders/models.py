from django.db import models

# Create your models here.
class Toppings(models.Model):
   types = models.CharField(max_length=64)
   def __str__(self):
      return f"This topping is called {self.types}"

# class Additions(models.Model):
#    types = models.CharField(max_length=64)
#    def __str__(self):
#       return f"This addition is called {self.types}"

class Menu(models.Model):
   category = models.CharField(max_length=64)
   main = models.CharField(max_length=64)
   size = models.CharField(max_length=64, null=True)
   price = models.DecimalField(max_digits=10, decimal_places=2)
 #  topping = models.ForeignKey(Toppings, on_delete=models.DO_NOTHING, null=True)

   def __str__(self):
      return f"{self.id} - {self.category} for {self.main}: {self.size} price is ${self.price}"


class Orders(models.Model):
   user = models.CharField(max_length=64, null=True)
   total = models.DecimalField(max_digits=20, decimal_places=2, null=True)
   products = models.CharField(max_length=64, null=True)
   description = models.CharField(max_length=128 , null=True)
   quantity = models.CharField(max_length=64, null=True)
   subtotal = models.CharField(max_length=64, null=True)
   price = models.CharField(max_length=64, null=True)
   status = models.CharField(max_length=64, default="pending")
   def products_list(self):
      return self.products.split(',')
   def description_list(self):
      return self.description.split(',') 
   def quantity_list(self):
      return self.quantity.split(',') 



class Cart(models.Model):
   user = models.CharField(max_length=64,null=True)
   category = models.CharField(max_length=64,null=True)
   main = models.CharField(max_length=64,null=True)
   topping = models.CharField(max_length=64, null=True)
   topping1 = models.CharField(max_length=64, null=True)
   topping2 = models.CharField(max_length=64, null=True)
   size = models.CharField(max_length=64, null=True)
   price = models.DecimalField(max_digits=20, decimal_places=2, null=True)
   def __str__(self):
      return f"{self.user} ordered for {self.category} with {self.main}: {self.size}  and topping of price {self.topping} is ${self.price}"



# class Orders(models.Model):
#    user = models.CharField(max_length=64, null=True)
#    name = models.CharField(max_length=64, , null=True)
#    email = models.CharField(max_length=64, null=True)
#    address = models.CharField(max_length=128 , null=True)
#    category = models.CharField(max_length=64, null=True)
#    main = models.CharField(max_length=64, null=True)
#    toppings = models.CharField(max_length=64, null=True)
#    size = models.CharField(max_length=64, null=True)
#    amount = models.DecimalField(max_digits=20, decimal_places=2, null=True)
#    date = models.CharField(max_length=64, null=True)
#    status = models.BooleanField(default=False, null=True)