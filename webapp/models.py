from django.db import models
from django.contrib.auth.models import User

class formDetails(models.Model):
    name=models.CharField(max_length=50)
    dob=models.DateField(editable=True)
    email=models.EmailField()
    mobile=models.CharField(max_length=20)
    address=models.TextField()
    photo=models.ImageField(upload_to='images/', null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    reg_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} {self.name}'
       
    
