from django.db import models



DISTRICT_CHOICES = (
    ('Kottayam', 'Kottayam'),
    ('Ernakulam', 'Ernakulam'),
    ('Kollam', 'Kollam'),
    ('Malappuram', 'Malappuram'),
    ('Kannur', 'Kannur'),
)

BRANCH_CHOICES = (
    ('Alanallur', 'Alanallur'),
    ('Calicut', 'Calicut'),
    ('Aluva', 'Aluva'),
    ('Edapally', 'Edapally'),
    ('Cannanore', 'Cannanore'),
)
ACCOUNT_TYPE =(
    ('Savings Account' , 'Savings Account'),
    ('Current Account' ,'Current Account'),
)


class Customer(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.PositiveIntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=250)
    district = models.CharField(choices=DISTRICT_CHOICES, max_length=50)
    branch = models.CharField(choices=BRANCH_CHOICES, max_length=50)
    account_type = models.CharField(choices=ACCOUNT_TYPE, max_length=50)
    materials_provided = models.CharField(max_length=100, null=True)


    def __str__(self):
        return (f"{self.name}  {self.email}")



