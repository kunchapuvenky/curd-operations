from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length


# Create your views here.

def DEPT(request):
    DT=DEPT_TABLE.objects.all()
    DT=DEPT_TABLE.objects.filter(LOC='BOTSON')

    d={'table':DT}
    return render(request,'DEPT_TABLE.html',d)

def EMP(request):
    ET=EMP_TABLE.objects.all()
    ET=EMP_TABLE.objects.filter(MGR=7698)
    ET=EMP_TABLE.objects.filter(EMPNO=7698)
    ET=EMP_TABLE.objects.filter(JOB='MANAGER')
    ET=EMP_TABLE.objects.order_by('EMPNO')
    ET=EMP_TABLE.objects.order_by('-ENAME')
    ET=EMP_TABLE.objects.order_by('-EMPNO')
    ET=EMP_TABLE.objects.order_by(Length('JOB'))
    ET=EMP_TABLE.objects.order_by(Length('ENAME'))
    #ET=EMP_TABLE.objects.order_by(Length('JOB')desc())
    #ET=EMP_TABLE.objects.exclude(JOB='CLERK')
    ET=EMP_TABLE.objects.all()
    ET=EMP_TABLE.objects.exclude(MGR=7698)
    ET=EMP_TABLE.objects.exclude(JOB='CLERK')
    ET=EMP_TABLE.objects.filter(EMPNO__gt=7654)
    #ET=EMP_TABLE.objects.filter(ENAME__gte=4)
    ET=EMP_TABLE.objects.filter(HIREDATE__day=17)
    ET=EMP_TABLE.objects.filter(HIREDATE__month=2)
    ET=EMP_TABLE.objects.filter(HIREDATE__year='1981')
    ET=EMP_TABLE.objects.filter(ENAME__startswith='J')
    ET=EMP_TABLE.objects.filter(ENAME__endswith='S')
    ET=EMP_TABLE.objects.filter(ENAME__in=('SMITH','ALLEN'))
    #ET=EMP_TABLE.objects.all()
    ET=EMP_TABLE.objects.filter(ENAME__contains='A')
    ET=EMP_TABLE.objects.filter(ENAME__regex=r'I')
    #ET=EMP_TABLE.objects.filter(ENAME='MILLER').update(ENAME='JONES')
    
    
    

    d={'table':ET}
    return render(request,'EMP_TABLE.html',d)