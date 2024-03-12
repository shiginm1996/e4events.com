from django.db import models


# Create your models here.

class register(models.Model):
    profile=models.FileField(upload_to='eventapp/static')
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    choice=[
        ('Kasargod','Kasargod'),
        ('Kannur', 'Kannur'),
        ('Kozhikode', 'Kozhikode'),
        ('Wayanad', 'Wayanad'),
        ('Malappuram', 'Malappuram'),
        ('Thrissur', 'Thrissur'),
        ('Palakkad', 'Palakkad'),
        ('Thrissur', 'Thrissur'),
        ('Eranakulam', 'Eranakulam'),
        ('Kottayam', 'Kottayam'),
        ('Alappuzha', 'Alappuzha'),
        ('Pathanamthitta', 'Pathanamthitta'),
        ('Kollam', 'Kollam'),
        ('Thiruvananthapuram', 'Thiruvananthapuram')

    ]
    district=models.CharField(max_length=50,choices=choice)
    choice1=[
        ('company','company'),
        ('customer','customer')
    ]
    usertype=models.CharField(max_length=50,choices=choice1)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    email=models.EmailField()
    website=models.CharField(max_length=50)
    phone=models.IntegerField()
    def __str__(self):
        return self.username


class eventbookmodel(models.Model):
    first_name=models.CharField(max_length=50)
    choice=[
        ('Wedding','Wedding'),
        ('Reception','Reception'),
        ('Engagement','Engagement'),
        ('House warming','House warming'),
        ('Bachelor party','Bachelor party'),
        ('Birthday part','Birthday part'),
        ('Others','Others')
    ]
    event_type=models.CharField(max_length=50,choices=choice)
    event_team=models.CharField(max_length=100)
    email=models.EmailField()
    address=models.CharField(max_length=100)
    event_date=models.DateField()
    phone=models.IntegerField()
    alternate_phone=models.IntegerField()
    amount=models.IntegerField()
    description=models.CharField(max_length=100)
    # def __str__(self):
    #     return self.first_name


class confirm_booking_model(models.Model):
    customer_name=models.CharField(max_length=50)
    event_type=models.CharField(max_length=50)
    email=models.EmailField()
    address=models.CharField(max_length=100)
    date_of_booking=models.DateField()
    event_date=models.DateField()
    phone=models.IntegerField()
    altern_phone=models.IntegerField()
    exp_amount=models.IntegerField()
    description=models.CharField(max_length=100)
    choice=[
        ('accept','accept'),
        ('reject','reject')
    ]
    confirm_order=models.CharField(max_length=50,choices=choice)
    event_team=models.CharField(max_length=50)


class reviewmodel(models.Model):
    cust_name=models.CharField(max_length=100)
    event_teams=models.CharField(max_length=100)
    choice=[
        ('5star','5star'),
        ('4star','4star'),
        ('3star', '3star'),
        ('2star', '2star'),
        ('1star', '1star'),
    ]
    rating=models.CharField(max_length=50,choices=choice)
    review=models.CharField(max_length=400)

    def __str__(self):
        return self.cust_name


class admin_model(models.Model):
    user_name=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.user_name









