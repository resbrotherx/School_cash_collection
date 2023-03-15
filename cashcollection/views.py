from django.shortcuts import render
import requests
from django.http import HttpResponse,HttpResponse,HttpResponseRedirect,JsonResponse

def login(request):
    return render(request,"sign-in.html")

def log(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password1']
        if email == "":
            respons = 'Error! Please enter Email its required !!'
        else:
            url = "http://188.166.99.136:5002/auth/login"
            datas = {
                "email":email,
                "password": password,
            }
            res = requests.post(url,headers={'Content-type':'application/json'},json=datas)
            try:
                if res.status_code == 201:
                    data = res.json()
                    request.session['token'] = data["accessToken"]
                    respons = "User login Successfully"
                else:
                    respons = "",data["message"]
            except Exception as e:
                respons = str(e)
        return HttpResponse(respons)

def dashboard(request):
    return render(request,"school_home.html")

def create_class(request):
    return render(request,"add-class.html")

def all_classes(request):
    request.session['token'] = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NCwiZW1haWwiOiJ0b255MTIzQGdtYWlsLmNvbSIsInJvbGUiOiJTY2hvb2wiLCJpYXQiOjE2Nzg4NjU3NDcsImV4cCI6MTY3ODg2OTM0N30.qmQNJarrWlL5-UX_D1i8RhyP12EIIgSF4JwOJYmzCB8"
    url = "http://188.166.99.136:5002/config/get-classes"
    header = {'Authorization':"Bearer %s" % (request.session['token']),'Content-type':'application/json'}
    rec = requests.get(url,headers=header)
    # tr_table = []

    if rec.status_code == 200:
        result = rec.json()
        if result["status"] == True:
            tr_table = result['data']
    else:
        return JsonResponse([{"message":"error","code":rec.status_code}],safe=False)
    context={
        "table":tr_table,
    }
    return render(request,"all_classes.html",context)

def all_student(request):
    request.session['token'] = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NCwiZW1haWwiOiJ0b255MTIzQGdtYWlsLmNvbSIsInJvbGUiOiJTY2hvb2wiLCJpYXQiOjE2Nzg4NjEwNjAsImV4cCI6MTY3ODg2NDY2MH0.MNH8o-hx4AA_fzkLgp0K8Q-qVKTfDDCaBkru3uSipwM"
    url = "http://188.166.99.136:5002/students/get-students"
    header = {'Authorization':"Bearer %s" % (request.session['token']),'Content-type':'application/json'}
    rec = requests.get(url,headers=header)
    # tr_table = []

    if rec.status_code == 200:
        result = rec.json()
        if result["status"] == True:
            # print("this the result here thanks",result)
            # print("this the result here thanks",result['data'])
            tr_table = result['data'] 
            # totalcount = result['data']["totalPages"]
    else:
        return JsonResponse([{"message":"error","code":rec.status_code}],safe=False)
    context={
        "table":tr_table,
    }
    return render(request,"students.html",context)

def create_student(request):
    return render(request,"add-students.html")

def signup(request):
    return render(request,"sign-up.html")


def create(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password1']
        school = request.POST['school']
        role = request.POST['role']
        phone_no = request.POST['phone_no']
        if email == "":
            respons = 'Error! Please add Email its required !!'
        else:
            url = "http://188.166.99.136:5002/users/create-user"
            data = {
                    "first_name":first_name,
                    "last_name":last_name,
                    "email":email,
                    "password":password,
                    "school":school,
                    "role":role,
                    "phone_no":phone_no
                }
            res = requests.post(url,headers={'Content-type':'application/json'},json=data)
            try:
                if res.status_code == 201:
                    data = res.json()
                    respons = 'Success! Your Account was created succefully'
                else:
                    respons = "",data["message"]
            except Exception as e:
                respons = str(e)
        return HttpResponse(respons)


def creat_class_api(request):
    if request.method == 'POST':
        class_name = request.POST['class']

        if class_name == "":
            respons = 'Error! Please enter class_name its required !!'
        else:
            request.session['token'] = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NCwiZW1haWwiOiJ0b255MTIzQGdtYWlsLmNvbSIsInJvbGUiOiJTY2hvb2wiLCJpYXQiOjE2Nzg4NjUzMjEsImV4cCI6MTY3ODg2ODkyMX0.PIMqETKj7GQ2S-e5TRpoYC_CJ9eAkPDxiOLDWoC_ac0"
            url = "http://188.166.99.136:5002/config/create-class"
            header = {'Authorization':"Bearer %s" % (request.session['token']),'Content-type':'application/json'}
            
            files = {"name":class_name}
            res = requests.post(url,headers=header,json=files)
            try:
                if res.status_code == 201:
                    data = res.json()
                    return HttpResponse("Class was created Successfully")
                else:
                    return HttpResponse("Error",data["message"])
            except Exception as e:
                respons = str(e)
        





def creat_student_api(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']
        last_name = request.POST['last_name']
        debt = request.POST['debt']

        if first_name == "" or last_name == "":
            return HttpResponse('Error! Please enter first_name and last_name its required !!')
        else:
            request.session['token'] = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NCwiZW1haWwiOiJ0b255MTIzQGdtYWlsLmNvbSIsInJvbGUiOiJTY2hvb2wiLCJpYXQiOjE2Nzg4NjEwNjAsImV4cCI6MTY3ODg2NDY2MH0.MNH8o-hx4AA_fzkLgp0K8Q-qVKTfDDCaBkru3uSipwM"
            url = "http://188.166.99.136:5002/students/create-student"
            header = {'Authorization':"Bearer %s" % (request.session['token']),'Content-type':'application/json'}
            
            files = {
                "first_name": first_name,
                "middle_name": middle_name,
                "last_name": last_name,
                "debt": debt,
                }
            res = requests.post(url,headers=header,json=files)
            try:
                if res.status_code == 201:
                    data = res.json()
                    return HttpResponse("Student has been created Successfully")
                else:
                    return HttpResponse(data["message"])
            except Exception as e:
                respons = str(e)
        
