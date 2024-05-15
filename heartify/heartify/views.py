from django.shortcuts import render
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from heart.forms import  HeartDiseaseForm
from heart.models import statis,Doctorsugg,appoint

from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.models import User, Group
from django.contrib import messages
User = get_user_model() 
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    user = request.user  # Retrieve the logged-in user
    context = {
        'user': user  # Pass the user object to the template
    }
    return render(request, 'home.html', context)




def SignupPage(request):
    if request.method == 'POST':
        # Retrieve form data
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        profile_picture = request.FILES.get('profile')
        user_type = request.POST.get('userType')  # Retrieve user type

        if password1 != password2:
            return HttpResponse("Your password and confirm password are not the same!!")
        else:
            try:
                # Create a user object
                my_user = User.objects.create_user(
                    username=username,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    #address=address,
                    #city=city,
                    #state=state,
                    #pincode=pincode,
                    #profile_picture=profile_picture
                )

                # Set user password
                my_user.set_password(password1)
                my_user.save()  # Save the user

                # Assign user to the selected group (patient or doctor)
                group = Group.objects.get(name=user_type)
                group.user_set.add(my_user)

                return redirect('doclogin')

            except Group.DoesNotExist:
                messages.error(request, 'Group does not exist. Please select a valid group.')
                # Redirect back to signup page or handle the error appropriately
                return redirect('')
            except Exception as e:
                messages.error(request, f'An error occurred: {str(e)}')
                # Redirect back to signup page or handle the error appropriately
                return redirect('')

    return render(request, 'register.html')


def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('heart')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

#@login_required(login_url='login')
def heart(request):
    user = request.user
    
	# Read the heart disease training data from a CSV file
    df = pd.read_csv('static/heart.csv')
    data = df.values
    X = data[:, :-1] # Input features (all columns except the last one)
    Y = data[:, -1:] # Target variable (last column)


    value = ''
    
    if request.method == 'POST':
		# Retrieve the user input from the form
        age = float(request.POST['age'])
        sex = float(request.POST['sex'])
        cp = float(request.POST['cp'])
        trestbps = float(request.POST['trestbps'])
        chol = float(request.POST['chol'])
        fbs = float(request.POST['fbs'])
        restecg = float(request.POST['restecg'])
        thalach = float(request.POST['thalach'])
        exang = float(request.POST['exang'])
        oldpeak = float(request.POST['oldpeak'])
        slope = float(request.POST['slope'])
        ca = float(request.POST['ca'])
        thal = float(request.POST['thal'])
        re=statis.objects.create(username=user,age=age,gender=sex,cp=cp,trestbps=trestbps,cholestrol=chol,fbs=fbs,restecg=restecg,thalach=thalach,exang=exang,oldpeak=oldpeak,slope=slope,ca=ca,thal=thal)
        re.save()

		# Create a numpy array with the user's data
        user_data = np.array(
			(age,
			sex,
			cp,
			trestbps,
			chol,
			fbs,
			restecg,
			thalach,
			exang,
			oldpeak,
			slope,
			ca,
			thal)
		).reshape(1, 13)

		# Create and train a Random Forest Classifier model
        rf = RandomForestClassifier(
			n_estimators=16,
			criterion='entropy',
			max_depth=9
		)

        rf.fit(np.nan_to_num(X), Y) # Train the model using the training data
        rf.score(np.nan_to_num(X), Y) # Evaluate the model's accuracy
        predictions = rf.predict(user_data) # Make predictions on the user's data

        if int(predictions[0]) == 1:
          value = 'have' # User is predicted to have heart disease
        elif int(predictions[0]) == 0:
          value = "don't have" # User is predicted to not have heart disease
    
    return render(request,
				'index.html',
				{
					'context': value,
					'title': 'Heart Disease Prediction',
					'active': 'btn btn-success peach-gradient text-white',
					'heart': True,
					'form': HeartDiseaseForm(),
                    "User":User
				})

def report(request):
    qs=statis.objects.all()
    
    list=["Monday","Tuesday","Wednesday","Thrusday","Friday","Saturday","Sunday"]
    context = {
        "list":list, # Pass the user object to the template
        
        "results":qs
    }
    return render(request,"statiscicalprofile.html",context)


def doctorslist(request):
    dr=Doctorsugg.objects.all()
    st=Doctorsugg.objects.filter(Status="True")
    
    context = {
        
        "Doctor":dr,
        
    }
    return render(request,"doctorpage.html",context)

def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged-out successfully")
    return redirect("heart")

def appointment(request):
    doctor=Doctorsugg.objects.all()
    Doctor=request.POST.get('DOC')
    time=request.POST.get('timing')
    date=request.POST.get('appdate')
    problem=request.POST.get('problm')
    user = request.user
    app=appoint.objects.create(name=user,dateofappointment=date,timeofappointment=time,doctorname=Doctor,Description=problem)
    app.save()
    return render(request,"appointmentpage.html",{ "Doctor":doctor})
    
def dashdoc(request):
    doc=Doctorsugg.objects.get(Doctorname=request.user)
    context={
        "doct":doc
	}
    return render(request,'dashboarddoc.html',context)

def update(request):
    doct=Doctorsugg.objects.get(Doctorname=request.user)
    context={
        "doco":doct
	}
    return render(request,"updatedoc.html",context)

def updatedoc(request):
    if request.method=="POST":
        name=request.POST.get("docname")
        Desig=request.POST.get("Deg")
        contact=request.POST.get("ph")
        email=request.POST.get("Email")
        addr=request.POST.get("add")
        status=request.POST.get("status")
        member=Doctorsugg.objects.get(Doctorname=request.user)
        member.Doctorname=name
        member.Designation=Desig
        member.phoneno=contact
        member.emailid=email
        member.Address=addr
        member.Status=status
        member.save()
        return redirect("dash")
        
def doctorlogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('dash')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'doctor login page.html')

def doctorapp(request):
    app=appoint.objects.get(doctorname=request.user)
    contex={"app":app}
    return render(request,"doctorappoints.html",contex)