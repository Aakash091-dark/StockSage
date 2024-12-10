from django.db import models

class Inventory(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

class SalesHistory(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    quantity_sold = models.IntegerField()
    sale_date = models.DateField()

    def __str__(self):
        return f"Sold {self.quantity_sold} of {self.inventory.name}"

