from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.models import *
from django.db.models import Q

def display_dept(request):
    QLDO=Dept.objects.all()
    d={'QLDO':QLDO}
    return render(request,'display_dept.html',d)

def display_emp(request):
    QLEO=Emp.objects.all()
    QLEO=Emp.objects.filter(Sal__gt=20000)
    QLEO=Emp.objects.filter(HIREDATE__year=2023)
    QLEO=Emp.objects.filter(HIREDATE__month=11)
    QLEO=Emp.objects.filter(HIREDATE__day__gt=6)
    QLEO=Emp.objects.filter(Ename__startswith='s')
    QLEO=Emp.objects.filter(Job__contains='s')
    QLEO=Emp.objects.filter(Job__endswith='g')
    QLEO=Emp.objects.filter(Job__endswith='k')
    QLEO=Emp.objects.filter(Job__in=('clerk','hr','testing'))
    QLEO=Emp.objects.filter(Ename='suresh',DEPTNO=890)
    QLEO=Emp.objects.filter(Q(Job='Sales')& Q(DEPTNO=56) & Q(Sal__gt=2500))
    QLEO=Emp.objects.filter(Q(HIREDATE='2023-10-02')& Q(DEPTNO=12) & Q( comm__gt=100))
    QLEO=Emp.objects.filter(Q(Ename='suresh')|Q(Job='clerk'))
    d={'QLEO':QLEO}
    return render(request,'display_emp.html',d)

def insert_dept(request):
    dn=int(input('enter the deptno:'))
    n=input('Enter the dept name:')
    l=input('Enter the Location:')
    ndo=Dept.objects.get_or_create(DEPTNO=dn,DNAME=n,Loc=l)[0]
    ndo.save()
    QLDO=Dept.objects.all()
    d={'QLDO':QLDO}
    return render(request,'display_dept.html',d)

def insert_emp(request):
    en=int(input('enter the empno:'))
    n=input('Enter the emp name:')
    j=input('Enter the job:')
    m=int(input('enter the mgrno:'))
    h=input('Enter the date:')
    s=int(input('enter the Salary:'))
    c=int(input('enter the comm:'))
    dn=int(input('Enter the dept no:'))
    DO=Dept.objects.get(DEPTNO=dn)
    NEO=Emp.objects.get_or_create(EMPNO=en,Ename=n,Job=j,Mgr=m,HIREDATE=h,Sal=s,comm=c,DEPTNO=DO)[0]
    NEO.save()
    QLEO=Emp.objects.all()
    d={'QLEO':QLEO}
    return render(request,'display_emp.html',d)




