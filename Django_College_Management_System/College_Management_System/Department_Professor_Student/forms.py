from django import  forms
from .models import Department,Professor,Student

class DepartmentModelForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

class ProfessorModelForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'