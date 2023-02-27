from django.db import models

from django.db import models

class MyTable(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    score = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = 'mytable'

