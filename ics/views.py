from turtle import end_fill
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.
import pandas as pd
import pickle
from joblib import load
from .models import Student
import csv
from io import StringIO

# IMPORT MODELS HERE
#model1 = pickle.load(open("modelIT.pkl", "rb"))
#model2 = pickle.load(open("modelCS.pkl", "rb"))
model1 = pickle.load(open("CS1stYear.pkl", "rb"))
model2 = pickle.load(open("CS2ndYear_1st.pkl", "rb"))
model3 = pickle.load(open("CS2ndYear_2nd.pkl", "rb"))
model4 = pickle.load(open("CS3rdYear_1st.pkl", "rb"))
model5 = pickle.load(open("CS3rdYear_2nd.pkl", "rb"))
model6 = pickle.load(open("CS4thYear.pkl", "rb"))
model7 = pickle.load(open("1stYear_IT.pkl", "rb"))
model8 = pickle.load(open("2ndYear_1st_IT.pkl", "rb"))
model9 = pickle.load(open("2ndYear_2nd_IT.pkl", "rb"))
model10 = pickle.load(open("3rdYear_1st_IT.pkl", "rb"))
model11 = pickle.load(open("3rdYear_2nd_IT.pkl", "rb"))
model12 = pickle.load(open("4thYear_1st_IT.pkl", "rb"))

# /IMPORT MODELS HERE

def index(request):
    return render(request, "index.html") 

# BSCS
def CSpage(request):
    return render(request, "CSpage.html")

def CS1_2page(request):
    return render(request, "CS1_2page.html")

def CS2page(request):
    return render(request, "CS2page.html")

def CS2_2page(request):
    return render(request, "CS2_2page.html")

def CS3page(request):
    return render(request, "CS3page.html")

def CS3_2page(request):
    return render(request, "CS3_2page.html")
# /BSCS

# BSIT
def ITpage(request):
    return render(request, "ITpage.html")

def IT1_2page(request):
    return render(request, "IT1_2page.html")

def IT2page(request):
    return render(request, "IT2page.html")

def IT2_2page(request):
    return render(request, "IT2_2page.html")

def IT3page(request):
    return render(request, "IT3page.html")

def IT3_2page(request):
    return render(request, "IT3_2page.html")
# /BSIT

#generate predictions

def csvUpload(request):
    if request.method == "POST":
        
        csv_file = request.FILES["csv_upload"]
        
        file = csv_file.read().decode("utf-8")
        
        prediction = model1.predict([[CC100,CC101]])
        studentID = request.POST['studentID']
        
        student1 = Student.objects.get(pk=1)
        student1.idNumber = studentID
        student1.result = prediction
        student1.CC100=CC100
        student1.CC101=CC101
        
        student1.save()

    return render(request, "rCS1_1.html" , {'student1': student1})
    

#CS_1.1
def resultCS1_1(request):
    if request.method == 'POST':
        CC100 = request.POST['CC100']
        CC101 = request.POST['CC101']
        
        prediction = model1.predict([[CC100,CC101]])
        studentID = request.POST['studentID']
        
        student1 = Student.objects.get(pk=1)
        student1.idNumber = studentID
        student1.result = prediction
        student1.CC100=CC100
        student1.CC101=CC101
        
        student1.save()

    return render(request, "rCS1_1.html" , {'student1': student1})

#CS_1.2
def resultCS1_2(request):
    CC102 = request.POST['CC102']
    CS111 = request.POST['CS111']
    MATH103 = request.POST['MATH103']

    prediction = model2.predict([[CC102,CS111,MATH103]])
    studentID = request.POST['studentID']
    
    student1 = Student.objects.get(pk=1)
    student1.idNumber = studentID
    student1.result = prediction
    student1.CC102=CC102
    student1.CS111=CS111
    student1.MATH103=MATH103
        
    student1.save()
    
    return render(request, "rCS1_2.html" , {'student1': student1})

#CS_2.1
def resultCS2_1(request):
    CC103 = request.POST['CC103']
    CS121 = request.POST['CS121']
    CS123 = request.POST['CS123']
    CS125 = request.POST['CS125']
    CS127 = request.POST['CS127']
    MATH104 = request.POST['MATH104']

    prediction = model3.predict([[CC103,CS121,CS123,CS125,CS127,MATH104]])
    studentID = request.POST['studentID']
    
    student1 = Student.objects.get(pk=1)
    student1.idNumber = studentID
    student1.result = prediction
    student1.CC103=CC103
    student1.CS121=CS121
    student1.CS123=CS123
    student1.CS125=CS125
    student1.CS127=CS127
    student1.MATH104=MATH104
    
    student1.save()
    
    return render(request, "rCS2_1.html" , {'student1': student1})

#CS_2.2
def resultCS2_2(request):
    CC104 = request.POST['CC104']
    CS120 = request.POST['CS120']
    CS122 = request.POST['CS122']
    CS124 = request.POST['CS124']
    CS126 = request.POST['CS126']

    prediction = model4.predict([[CC104,CS120,CS122,CS124,CS126]])
    studentID = request.POST['studentID']
    
    student1 = Student.objects.get(pk=1)
    student1.idNumber = studentID
    student1.result = prediction
    student1.CC104=CC104
    student1.CS120=CS120
    student1.CS122=CS122
    student1.CS124=CS124
    student1.CS126=CS126
    
    student1.save()
    
    return render(request, "rCS2_2.html" , {'student1': student1})

#CS_3.1
def resultCS3_1(request):
    CC105 = request.POST['CC105']
    CS131 = request.POST['CS131']
    CS135 = request.POST['CS135']
    CS137 = request.POST['CS137']

    prediction = model5.predict([[CC105,CS131,CS135,CS137]])
    studentID = request.POST['studentID']
    
    student1 = Student.objects.get(pk=1)
    student1.idNumber = studentID
    student1.result = prediction
    student1.CC105=CC105
    student1.CS131=CS131
    student1.CS135=CS135
    student1.CS137=CS137
    
    student1.save()
    
    return render(request, "rCS3_1.html" , {'student1': student1})

#CS_3.2
def resultCS3_2(request):
    CS130 = request.POST['CS130']
    CS132 = request.POST['CS132']
    CS134 = request.POST['CS134']
    CS136 = request.POST['CS136']

    prediction = model6.predict([[CS130,CS132,CS134,CS136]])
    studentID = request.POST['studentID']
    
    student1 = Student.objects.get(pk=1)
    student1.idNumber = studentID
    student1.result = prediction
    student1.CS130=CS130
    student1.CS132=CS132
    student1.CS134=CS134
    student1.CS136=CS136
    
    student1.save()
    
    return render(request, "rCS3_2.html" , {'student1': student1})

#IT_1.1
def resultIT1_1(request):
    CC100 = request.POST['CC100']
    CC101 = request.POST['CC101']

    prediction = model7.predict([[CC100,CC101]])
    studentID = request.POST['studentID']
    
    student1 = Student.objects.get(pk=1)
    student1.idNumber = studentID
    student1.result = prediction
    student1.CC100=CC100
    student1.CC101=CC101
    
    student1.save()
    
    return render(request, "rIT1_1.html" , {'student1': student1})

#IT_1.2
def resultIT1_2(request):
    CC102 = request.POST['CC102']
    IT112 = request.POST['IT112']
    IT114 = request.POST['IT114']
    MATH103 = request.POST['MATH103']
    
    prediction = model8.predict([[CC102,IT112,IT114,MATH103]])
    studentID = request.POST['studentID']
    
    student1 = Student.objects.get(pk=1)
    student1.idNumber = studentID
    student1.result = prediction
    student1.CC102=CC102
    student1.IT112=IT112
    student1.IT114=IT114
    student1.MATH103=MATH103
    
    student1.save()
    
    return render(request, "rIT1_2.html" , {'student1': student1})

#IT_2.1
def resultIT2_1(request):
    CC103 = request.POST['CC103']
    IT121 = request.POST['IT121']
    IT144 = request.POST['IT144']
    MATH104 = request.POST['MATH104']
    
    prediction = model9.predict([[CC103,IT121,IT144,MATH104]])
    studentID = request.POST['studentID']
    
    student1 = Student.objects.get(pk=1)
    student1.idNumber = studentID
    student1.result = prediction
    student1.CC103=CC103
    student1.IT121=IT121
    student1.IT144=IT144
    student1.MATH104=MATH104
    
    student1.save()
    
    return render(request, "rIT2_1.html" , {'student1': student1})

#IT_2.2
def resultIT2_2(request):
    CC104 = request.POST['CC104']
    IT122 = request.POST['IT122']
    IT124 = request.POST['IT124']
    IT126 = request.POST['IT126']
    
    prediction = model10.predict([[CC104,IT122,IT124,IT126]])
    studentID = request.POST['studentID']
    
    student1 = Student.objects.get(pk=1)
    student1.idNumber = studentID
    student1.result = prediction
    student1.CC104=CC104
    student1.IT122=IT122
    student1.IT124=IT124
    student1.IT126=IT126
    
    student1.save()
    
    return render(request, "rIT2_2.html" , {'student1': student1})

#IT_3.1
def resultIT3_1(request):
    CC105 = request.POST['CC105']
    IT131 = request.POST['IT131']
    IT133 = request.POST['IT133']
    IT135 = request.POST['IT135']
    IT137 = request.POST['IT137']
    
    prediction = model11.predict([[CC105,IT131,IT133,IT135,IT137]])
    studentID = request.POST['studentID']
    
    student1 = Student.objects.get(pk=1)
    student1.idNumber = studentID
    student1.result = prediction
    student1.CC105=CC105
    student1.IT131=IT131
    student1.IT133=IT133
    student1.IT135=IT135
    student1.IT137=IT137
    
    student1.save()
    
    return render(request, "rIT3_1.html" , {'student1': student1})

#IT_3.2
def resultIT3_2(request):
    IT132 = request.POST['IT132']
    IT134 = request.POST['IT134']
    IT136 = request.POST['IT136']
    
    prediction = model12.predict([[IT132,IT134,IT136]])
    studentID = request.POST['studentID']
    
    student1 = Student.objects.get(pk=1)
    student1.idNumber = studentID
    student1.result = prediction
    student1.IT132=IT132
    student1.IT134=IT134
    student1.IT136=IT136
    
    student1.save()
    
    return render(request, "rIT3_2.html" , {'student1': student1})
