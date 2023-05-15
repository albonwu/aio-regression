from django.db import models

# Create your models here.
class Coordinate(models.Model):
    x = models.FloatField()
    y = models.FloatField()

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    
class Params(models.Model):
    m = models.FloatField()
    b = models.FloatField()

    def __str__(self):
        return "y = " + str(self.m) + "x + " + str(self.b)