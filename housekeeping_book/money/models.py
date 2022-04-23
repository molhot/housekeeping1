from django.db import models

# Create your models here.

class Money(models.Model):
    use_date = models.DateTimeField('date')
    detail = models.CharField(max_length=200)
    cost = models.IntegerField(default=0)

    def __str__(self):
        return self.detail + '￥' + str(self.cost)