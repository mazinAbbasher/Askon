from django.db import models

class State(models.Model):
    name = models.CharField(max_length=30)
    name_english = models.CharField(max_length=30)
    sequence = models.IntegerField(default = 100)


    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=30)
    name_english = models.CharField(max_length=30)
    state = models.ForeignKey(State,on_delete=models.PROTECT)
    sequence = models.IntegerField(default = 100)
    is_available = models.BooleanField(default=True)
    



    def __str__(self):
        return self.name

class Owner(models.Model):
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=20)
    another_phone = models.CharField(max_length=25)


    def __str__(self):
        return self.name

class House(models.Model):
    TYPES = {
        "1":"سكني" ,
        "2":"تجاري",
        "3":"زراعي",
    }
    region = models.ForeignKey(Region,on_delete=models.PROTECT)
    rooms = models.IntegerField(default=0)
    ready = models.BooleanField(default=False)
    price = models.IntegerField()
    for_sale = models.BooleanField(default=False)
    for_rent = models.BooleanField(default=True)
    is_available = models.BooleanField(default=True)
    description = models.CharField(max_length=600)
    area = models.CharField(max_length=25)
    owner = models.ForeignKey(Owner,on_delete=models.PROTECT)
    sequence = models.IntegerField(default = 100)
    main_image = models.ImageField(upload_to='images/',null=True,blank=True)
    sale_price = models.IntegerField(default=0,null=True)
    date = models.DateTimeField(auto_now=True,null=True)
    type = models.TextField(null=False, choices=TYPES, default="1")
    private_description = models.CharField(max_length=500,default="")
    unit = models.CharField(max_length=50,default="م")
    





    def __str__(self):
        return str(self.pk)

class Image(models.Model):
    house = models.ForeignKey(House,on_delete=models.PROTECT)
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    sequence = models.IntegerField(default = 100)


class Message(models.Model):
    phone = models.CharField(max_length=20)
    message = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now=True,null=True)


class Order(models.Model):
    STATUS_CHOICES = [
        (1, 'initialized'),
        (2, 'done'),
        (3, 'canceled'),
    ]
    house = models.ForeignKey(House,on_delete=models.PROTECT)
    phone = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True,null=True)
    status  = models.IntegerField(default=1,choices=STATUS_CHOICES)



