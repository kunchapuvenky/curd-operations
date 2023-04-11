from django.db import models


# Create your models here.

class DEPT_TABLE(models.Model):
    DEPTNO=models.IntegerField(primary_key=True)
    DNAME=models.CharField(max_length=100,unique=True)
    LOC=models.CharField(max_length=100) 
    def __str__(self):
        return self.DNAME


class EMP_TABLE(models.Model):
    EMPNO=models.IntegerField(primary_key=True)
    ENAME=models.CharField(max_length=100,unique=True)
    JOB=models.CharField(max_length=100)
    MGR=models.IntegerField(null=True,blank=True)
    HIREDATE=models.DateField()
    SAL=models.IntegerField()
    COMM=models.IntegerField(null=True,blank=True)
    DEPTNO=models.ForeignKey(DEPT_TABLE,on_delete=models.CASCADE)
    def __str__(self):
        return self.ENAME
