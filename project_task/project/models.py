from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    Full_name = models.CharField(max_length=100,verbose_name="User Name")
    email = models.EmailField(max_length=255,blank=True, null=True, verbose_name="Email")
    Number = models.CharField(max_length=20, blank=True, null=True, verbose_name="Phone Number")

    
    def __str__(self) :
        return self.Full_name
    
# create model for client
class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="Client Name")
    email = models.EmailField(max_length=255, blank=True, null=True, verbose_name="Email")
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="Phone Number")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Last Updated At")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    
#create model for Project
class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name="Project Name")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Client")
    users = models.ManyToManyField(User,verbose_name='User')
    start_date = models.DateField(verbose_name="Start Date")
    end_date = models.DateField(verbose_name="End Date")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Last Updated At") 

    def __str__(self):
        return self.name
        # return self.client.name+"--"+self.users.name
    

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"