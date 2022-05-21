from django.db import models


# models for the entries app. Names subject to change.
class Warehouse(models.Model):
    """
    model representing any Warehouse.
    fields:
        name: the name of this warehouse location.
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        """
        represent this Warehouse as a string
        :return: a string containing this Warehouse's name and primary key
        """
        return str(self.name) + " (" + str(self.pk) + ")"


class Item(models.Model):
    """
    model representing any single item in the inventory.
    fields:
        name: the name of this item in inventory.
        arrival_date: the date that this item entered inventory.
        location: ForeignKey field to Warehouse. Many Items may have one Warehouse,
            so the field is in this model. Also, any Item may have *no* Warehouse,
            represented here as a null Warehouse for simplicity.
    """
    name = models.CharField(max_length=200)
    arrival_date = models.DateField('date added to inventory')
    location = models.ForeignKey(to=Warehouse, related_name='items_at_warehouse',
                                 on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """
        represent this item as a string
        :return: a string containing this item's name and primary key
        """
        return str(self.name) + " (" + str(self.pk) + ")"
