from django.shortcuts import render,redirect
from django.conf import settings
from .models import Employee,Admin


def home(request):
	return render(request,"home.html")
# Create your views here.

def signup(request):
	if request.method=="POST":
		try:
			emp=Employee.objects.get(email=request.POST['email'])
			msg="User already Registered!!"
			return render(request,"signup.html",{msg:'msg'})
		except:
			if request.POST['password']==request.POST['cpassword']:
				Employee.objects.create(
					firstname=request.POST['firstname'],
					lastname=request.POST['lastname'],
					email=request.POST['email'],
					mobile=request.POST['mobile'],
					gender=request.POST['gender'],
					address=request.POST['address'],
					password=request.POST['password'],
					cpassword=request.POST['cpassword'],
					image=request.FILES['image'],
					usertype=request.POST['usertype']
					)
				msg="Signup Successfully!!"
				return render(request,"login.html",{msg:'msg'})
			else:
				msg="Incorrect password!!"
				return render(request,"signup.html",{msg:'msg'})

	else:
		return render(request,"signup.html")

def login(request):
	if request.method=="POST":
		try:
			emp=Employee.objects.get(
				email=request.POST['email'],
				password=request.POST['password']
				)
			if emp.usertype=="user":
				request.session['email']=emp.email
				request.session['firstname']=emp.firstname
				request.session['image']=emp.image.url
				return render(request,"home.html")
			elif emp.usertype=="seller":
				request.session['email']=emp.email
				request.session['firstname']=emp.firstname
				request.session['image']=emp.image.url
				return render(request,"sellerhome.html")

		except:
			msg="email and password are incorrect"
			return render(request,"login.html",{'msg':msg})
	else:

		return render(request,"login.html")

def logout(request):
	try:
		del request.session['email']
		del request.session['firstname']
		del request.session['image']
		return render(request,'login.html')
	except:
		return redirect("logout")

def sellerhome(request):
	return render(request,"sellerhome.html")


def sellersignup(request):
	if request.method=="POST":
		try:
			emp=Employee.objects.get(email=request.POST['email'])
			msg="User already Registered!!"
			return render(request,"signup.html",{msg:'msg'})
		except:
			if request.POST['password']==request.POST['cpassword']:
				User.objects.create(
					firstname=request.POST['firstname'],
					lastname=request.POST['lastname'],
					email=request.POST['email'],
					mobile=request.POST['mobile'],
					gender=request.POST['gender'],
					address=request.POST['address'],
					password=request.POST['password'],
					cpassword=request.POST['cpassword'],
					image=request.FILES['image'],
					usertype=request.POST['usertype']
					)
				msg="Signup Successfully!!"
				return render(request,"login.html",{msg:'msg'})
			else:
				msg="Incorrect password!!"
				return render(request,"sellersignup.html",{msg:'msg'})

	else:
		return render(request,"sellersignup.html")

def seller_adddetails(request):
	if request.method=="POST":
		seller=Employee.objects.get(email=request.session['email'])
		Admin.objects.create(
				seller=seller,
				Company_name=request.POST['Company_name'],
				Company_address=request.POST['Company_address'],
				person_name=request.POST['person_name'],
				contact=request.POST['contact'],
				date_time=request.POST['date_time'],
				Comment_remark=request.POST['Comment_remark'],
				purpose=request.POST['purpose']


			)
		msg="Added Successfully!!"
		return render(request,"seller_adddetails.html",{'msg':msg})
	else:
 
		return render(request,"seller_adddetails.html")

def seller_viewdetails(request):
	seller=Employee.objects.get(email=request.session['email'])
	admin=Admin.objects.filter(seller=seller)
	return render(request,"seller_viewdetails.html",{'admin':admin})

def seller_Editdetails(request,pk):
	admin=Admin.objects.get(pk=pk)

	if request.method=="POST":
		admin.Company_name=request.POST['Company_name']
		admin.Company_address=request.POST['Company_address']
		admin.person_name=request.POST['person_name']	 	
		admin.date_time=request.POST['date_time']
		admin.contact=request.POST['contact']
		admin.Comment_remark=request.POST['Comment_remark']
		admin.purpose=request.POST['purpose']
		admin.save()	
		return render(request,"seller_viewdetails.html")
	else:
		msg="Updated Successfully!!"
		return render(request,"seller_Editdetails.html",{'admin':admin, 'msg':msg })

def seller_Deletedetails(request,pk):
	admin=Admin.objects.get(pk=pk)
	admin.delete()
	return redirect("seller_viewdetails")

def user_view_all_details(request):
	admin=Admin.objects.all()
	return render(request,"user_view_all_details.html",{'admin':admin})