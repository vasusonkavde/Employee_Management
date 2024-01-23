from django.shortcuts import render,HttpResponseRedirect
from .forms import EmployeeForm, DepartmentForm, EmployeeSalaryForm
from .models import *
from .forms import SalaryReportForm

# Create your views here.
def add_emp(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = EmployeeForm()
    
    data = Employee.objects.all()
    print(form.fields['reporting_manager'].queryset)  # Check the queryset for reporting_manager
    print(form.fields['department'].queryset)         # Check the queryset for department
    return render(request, 'add_emp.html', {'form': form, 'data': data})  

def delete_emp(request,id):
    if request.method=="POST":
        pi=Employee.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect( '/')
    

def update_emp(request,id):
    if request.method=='POST':
        pi=Employee.objects.get(pk=id)
        fm=EmployeeForm(request.POST,instance=pi)
        fm.save()
        return HttpResponseRedirect( '/')
    else:
        pi=Employee.objects.get(pk=id)
        fm=EmployeeForm(instance=pi)
        return render(request,'update_emp.html', {'fm':fm})  


# Department
def add_department(request):
    if request.method=='POST':
        form=DepartmentForm(request.POST)
        if form.is_valid():
            form.save() 
            return HttpResponseRedirect('/add_dept')
      
    else:
        form=DepartmentForm()
    data=Department.objects.all()
    return render(request,'add_department.html', {'form':form, 'data':data})  

def delete_department(request,id):
    if request.method=="POST":
        pi=Department.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect( '/add_dept')
    

def update_department(request,id):
    if request.method=='POST':
        pi=Department.objects.get(pk=id)
        fm=DepartmentForm(request.POST,instance=pi)
        fm.save()
        return HttpResponseRedirect( '/add_dept')
    else:
        pi=Department.objects.get(pk=id)
        fm=DepartmentForm(instance=pi)
        return render(request,'update_department.html', {'fm':fm})  


# salary
def add_salary(request):
    if request.method=='POST':
        form=EmployeeSalaryForm(request.POST)
        if form.is_valid():
            form.save() 
            return HttpResponseRedirect('/add_salary')
    else:
        form=EmployeeSalaryForm()
    data=EmployeeSalary.objects.all()
    return render(request,'add_salary.html', {'form':form, 'data':data})  

def delete_salary(request,id):
    if request.method=="POST":
        pi=EmployeeSalary.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect( '/add_salary')
    

def update_salary(request,id):
    if request.method=='POST':
        pi=EmployeeSalary.objects.get(pk=id)
        fm=EmployeeSalaryForm(request.POST,instance=pi)
        fm.save()
        return HttpResponseRedirect( '/add_salary')
    else:
        pi=EmployeeSalary.objects.get(pk=id)
        fm=EmployeeSalaryForm(instance=pi)
        return render(request,'update_salary.html', {'fm':fm})  


def salary_report(request):
    form = SalaryReportForm(request.GET or None)
    salary_data = []

    if form.is_valid():
        start_date = form.cleaned_data['start_date']
        end_date = form.cleaned_data['end_date']

        # Perform query to get department-wise salary data based on date range
        salary_data = get_salary_data(start_date, end_date)

    return render(request, 'salary_report.html', {'form': form, 'salary_data': salary_data})

def get_salary_data(start_date, end_date):
    # Perform your query to get department-wise salary data within the date range
    # Example query: EmployeeSalary.objects.filter(start_date__range=[start_date, end_date])
    # You might need to join with Employee and Department models

    # Assuming you have a 'cost' field in EmployeeSalary, adjust accordingly
    data = EmployeeSalary.objects.filter(
        start_date__range=[start_date, end_date]
    ).values('employee__department__name').annotate(total_cost=models.Sum('salary'))

    salary_data = [(entry['employee__department__name'], entry['total_cost']) for entry in data]
    return salary_data
