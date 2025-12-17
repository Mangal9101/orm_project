from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student
# Create your views here.
  
# to insert a data in a table
def add_student(request):
    if request.method=="POST":
        rn=request.POST.get('roll_no')
        nm=request.POST.get('name')
        cs=request.POST.get('course')
        fee=request.POST.get('fee')
        con=request.POST.get('contact')
        add=request.POST.get('address')

        Student.objects.create(roll_no=rn,name=nm,course=cs,fee=fee,contact=con,address=add)
        return HttpResponse("student save successfully")
    else:
        return render(request,'add_student.html') 

# To Read a data in a table
from django.db.models import Q
def show_student(request):
    
    # data=Student.objects.all()                       # sabhi data dikhane k liye
    # data=Student.objects.filter(roll_no=101)         # get humesha face karta hai single object
    # data=Student.objects.order_by('name','fee')      # arrange karne k liye
    # data=Student.objects.exclude(course="bsc")       # exclude chodne k liye hota hai
    # data=Student.objects.filter(name="gk",fee=5000)  # filter filter karne k liye name age etc se 
    # data=Student.objects.count()
    # # iexact and exact and contains
    # data=Student.objects.filter(name__exact='Mangal')     # Exact name k liye
    # data=Student.objects.filter(name__iexact='mangal')    # inexact name k liye isme bas upper & lower hi check karta hai
    # data=Student.objects.filter(name__contains='gk')      # contains me sabhi aa jata h jisme wo word ho
    # data=Student.objects.filter(name__startswith='m')
    # data=Student.objects.filter(name__endswith='k')
    # data=Student.objects.filter(name__startswith='m', name__endswith='l')


    # # i.e, bulk me data entry k liye :- 
    # data=[Student(roll_no="201",name="A",course="MCA",fee=12000,contact=12345,address="indore"),
    #       Student(roll_no="202",name="B",course="MCA",fee=12000,contact=12345,address="indore"),
    #       Student(roll_no="203",name="C",course="MCA",fee=12000,contact=12345,address="indore"),
    #       Student(roll_no="204",name="D",course="MCA",fee=12000,contact=12345,address="indore"),
    #       Student(roll_no="205",name="E",course="MCA",fee=12000,contact=12345,address="indore")]
    # Student.objects.bulk_create(data)


    # # i.e, for sigle data entry by user a run time
    # ob=Student(roll_no="206",name="A",course="MCA",fee=12000,contact=12345,address="indore")
    # ob.save()

    # # Q query that should me use to face a data by specific name and other fieldtype with the help of (and &) (or |)
    # q1=Q(name='A') & Q(address='indore')    ((    # or k liye |   # and k liye &    ))
    # data=Student.objects.filter(q1)

    # # Mysql li command line k liye raw use hota hai or raw k andar sql query
    # data= Student.objects.raw("select * from myapp_student where fee between 12000 and 18000")
    
    data=Student.objects.all()
    return render(request,'show_student.html',{'data':data})

# To Update a data in a table
def update_student(request,pk):
    if request.method=="POST":
        rn=request.POST.get('roll_no')
        nm=request.POST.get('name')
        cs=request.POST.get('course')
        fee=request.POST.get('fee')
        con=request.POST.get('contact')
        add=request.POST.get('address')
        Student.objects.filter(roll_no=rn).update(name=nm,course=cs,fee=fee,contact=con,address=add)
        return redirect('st_show')
    else:
        data=Student.objects.get(roll_no=pk)
        return render(request,'update_student.html',{'data':data})

# To Delete a data in a table
def delete_student(request,pk):
    Student.objects.filter(roll_no=pk).delete()
    return redirect('st_show')