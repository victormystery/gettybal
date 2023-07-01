from django.db import models



class LoanApplication(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    business_name = models.CharField(max_length=100)
    email = models.EmailField()
    business_phone = models.CharField(max_length=20)
    mobile_phone = models.CharField(max_length=20)
    credit_score = models.CharField(max_length=20)
    industry = models.CharField(max_length=100)
    time_business = models.CharField(max_length=100)
    anual_sales = models.CharField(max_length=100)
    monthly_gross = models.CharField(max_length=100)

    def __str__(self):
        return self.business_name


class Review(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    rating = models.IntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    