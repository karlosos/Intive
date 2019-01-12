from django.db import models


class Salary(models.Model):
    worked_years = models.FloatField()
    salary = models.FloatField()

    def __str__(self):
        return str(self.worked_years) + " " + str(self.salary)
