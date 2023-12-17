from django.db import models

# Create your models here.
class Dept(models.Model):
    DEPTNO=models.IntegerField(primary_key=True)
    DNAME=models.CharField(max_length=100)
    Loc=models.CharField(max_length=100)

    def __str__(self):
        return str(self.DEPTNO)
    
class Emp(models.Model):
    EMPNO=models.IntegerField(primary_key=True)
    Ename=models.CharField(max_length=100)
    Job=models.CharField(max_length=100)
    Mgr=models.IntegerField()
    HIREDATE=models.DateField()
    Sal=models.IntegerField()
    comm=models.IntegerField()
    DEPTNO=models.ForeignKey(Dept,on_delete=models.CASCADE)
    def __str__(self):
        return self.Ename