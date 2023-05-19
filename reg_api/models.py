from django.db import models

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
    
class QuadParams(models.Model):
    a = models.FloatField()
    b = models.FloatField()
    c = models.FloatField()

    def __str__(self):
        return "y = " + str(self.a) + "x^2 + " + str(self.b) + "x + " + str(self.c)