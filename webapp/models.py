from django.db import models

class gallary(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100) 
    pic=models.ImageField(upload_to="uploads/") 

    class Meta:
        db_table="gallarytb"   
    def __str__(self):
        return self.name
    

    
class sign(models.Model):
    id=models.AutoField(primary_key=True)
    Username=models.CharField(max_length=100)
    Email=models.EmailField()
    Password=models.CharField(max_length=45)
    Phone=models.CharField(max_length=55)
    Address=models.CharField(max_length=55)
    
    class Meta:
        db_table="signtb"

class jobmodel(models.Model):
    rid=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=100)
    Phone=models.CharField(max_length=55)
    Email=models.EmailField()
    Resume=models.ImageField(upload_to="uploads/")
    Pic=models.ImageField(upload_to="uploads/")
    Password=models.CharField(max_length=45)
    class Meta:
        db_table="jobtb"

class contactmodel(models.Model):
    id=models.AutoField(primary_key=True)
    Username=models.CharField(max_length=100)
    Email=models.EmailField()
    Phone=models.CharField(max_length=55)
    Message=models.CharField(max_length=100)
    
    class Meta:
        db_table="contacttb"   
class servicesmodel(models.Model) :
    id=models.AutoField(primary_key=True)
    Sname=models.CharField(max_length=100)
    pic=models.ImageField(upload_to="uploads/")
    title=models.TextField(null=True)

    class Meta:
        db_table="servicetb"     
  
class userservices(models.Model):
    id=models.AutoField(primary_key=True)
    sid=models.IntegerField()
    Sdate=models.DateTimeField(auto_now_add=True,editable='True' ,null=True)
    pic=models.ImageField(upload_to="uploads/")
    Sname=models.CharField(max_length=67, null=True)
    title=models.TextField(null=True)
    Name=models.CharField(max_length=100)
    Phone=models.CharField(max_length=55)
    Email=models.EmailField()
    Address=models.CharField(max_length=100)
    Message=models.CharField(max_length=100)
    class Meta:
        db_table="usersertb"
    


    
    
