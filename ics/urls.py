from django.urls import include, path
from django.shortcuts import redirect

from .views import index,CSpage,ITpage,CS1_2page,CS2page,CS2_2page,CS3page,IT1_2page,IT2page,IT2_2page,IT3page,CS3_2page,IT3_2page,resultCS1_1,resultCS1_2,resultCS2_1,resultCS2_2,resultCS3_1,resultCS3_2,resultIT1_1,resultIT1_2,resultIT2_1,resultIT2_2,resultIT3_1,resultIT3_2,csvUpload


from . import views

urlpatterns = [ 
    path('', index, name="index"),
    path('CSpage', CSpage, name = "CSpage"),
    path('CS1_2page', CS1_2page, name = "CS1_2page"),
    path('CS2page', CS2page, name = "CS2page"),
    path('CS2_2page', CS2_2page, name = "CS2_2page"),
    path('CS3page', CS3page, name = "CS3page"),
    path('CS3_2page', CS3_2page, name = "CS3_2page"),
    path('ITpage', ITpage, name = "ITpage"),
    path('IT1_2page', IT1_2page, name = "IT1_2page"),
    path('IT2page', IT2page, name = "IT2page"),
    path('IT2_2page', IT2_2page, name = "IT2_2page"),
    path('IT3page', IT3page, name = "IT3page"),
    path('IT3_2page', IT3_2page, name = "IT3_2page"),
    
    path('resultCS1_1', resultCS1_1, name = "resultCS1_1"),
    path('resultCS1_2', resultCS1_2, name = "resultCS1_2"),
    path('resultCS2_1', resultCS2_1, name = "resultCS2_1"),
    path('resultCS2_2', resultCS2_2, name = "resultCS2_2"),
    path('resultCS3_1', resultCS3_1, name = "resultCS3_1"),
    path('resultCS3_2', resultCS3_2, name = "resultCS3_2"),
    
    path('resultIT1_1', resultIT1_1, name = "resultIT1_1"),
    path('resultIT1_2', resultIT1_2, name = "resultIT1_2"),
    path('resultIT2_1', resultIT2_1, name = "resultIT2_1"),
    path('resultIT2_2', resultIT2_2, name = "resultIT2_2"),
    path('resultIT3_1', resultIT3_1, name = "resultIT3_1"),
    path('resultIT3_2', resultIT3_2, name = "resultIT3_2"),
    
    path('csvUpload', csvUpload, name = "csvUpload"),
]
