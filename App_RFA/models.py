from django.db import models

class Monthly(models.Model):
    Time_Period = models.CharField(max_length=100)
    Area = models.CharField(max_length=250)
    Sector = models.CharField(max_length=250)
    Project = models.CharField(max_length=100)
    Community = models.CharField(max_length=250)
    Results_Level = models.CharField(max_length=50)
    Frequency = models.CharField(max_length=100)
    Indicator_ID = models.CharField(max_length=50)
    Indicator = models.CharField(max_length=300)
    Activity = models.CharField(max_length=300)
    Unit = models.CharField(max_length=100)
    Actual = models.FloatField()
    Male_Under5 = models.FloatField()
    Female_Under5 = models.FloatField()
    Male_Above5 = models.FloatField()
    Female_Above5 = models.FloatField()
    Male_PWD = models.FloatField()
    Female_PWD = models.FloatField()
    created_at = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.Sector


class Target(models.Model):
    Time_Period = models.CharField(max_length=100)
    Area = models.CharField(max_length=250)
    Sector = models.CharField(max_length=250)
    Project = models.CharField(max_length=100)
    Community = models.CharField(max_length=250)
    Results_Level = models.CharField(max_length=50)
    Frequency = models.CharField(max_length=100)
    Indicator_ID = models.CharField(max_length=50)
    Indicator = models.CharField(max_length=300)
    Activity = models.CharField(max_length=300)
    Unit = models.CharField(max_length=100)
    Target = models.FloatField()
    def __str__(self):
        return self.Sector
