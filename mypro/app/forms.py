from django import forms
from app.models import Employee, Department, EmployeeSalary

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

class EmployeeSalaryForm(forms.ModelForm):
    class Meta:
        model = EmployeeSalary
        fields = '__all__'

class SalaryReportForm(forms.Form):
    start_date = forms.DateField(label='Start Date', widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(label='End Date', widget=forms.DateInput(attrs={'type': 'date'}))
