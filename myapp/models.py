from django.db import models

# Create your models here.
class Employee(models.Model):
	firstname=models.CharField(max_length=100)
	lastname=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	mobile=models.CharField(max_length=100)
	address=models.TextField()
	gender=models.CharField(max_length=100)
	password=models.CharField(max_length=100)
	cpassword=models.CharField(max_length=100)
	image=models.ImageField(upload_to="images/",default="",blank=True,null=True)
	status=models.CharField(max_length=100, default="inactive")
	usertype=models.CharField(max_length=100,default="user")


	def __str__(self):
		return self.firstname+"-"+self.lastname

class Admin(models.Model):

	seller=models.ForeignKey(Employee,on_delete=models.CASCADE)
	Company_name=models.CharField(max_length=100)
	purpose=models.CharField(max_length=100,default=True)
	Company_address=models.TextField()
	person_name=models.CharField(max_length=100)
	contact=models.IntegerField()
	date_time=models.TextField()
	Comment_remark=models.TextField()

	def __str__(self):
		return self.seller.firstname+" - "+self.Company_name
