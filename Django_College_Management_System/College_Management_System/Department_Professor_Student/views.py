from django.shortcuts import render,redirect
from .forms import DepartmentModelForm,ProfessorModelForm,StudentModelForm
from .models import Department,Professor,Student
from django.views import View

                                       ##########Department###############
class AddDepartmentView(View):
    def get(self,request):
        form = DepartmentModelForm()
        template_name = 'Department/adddepartmentform.html'
        context = {'form':form}
        return render(request, template_name, context)
    def post(self,request):
        form = DepartmentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_department")
        template_name = 'Department/adddepartmentform.html'
        context = {'form': form}
        return render(request, template_name, context)

class ShowDepartmentView(View):
    def get(self,request):
        department_obj = Department.objects.all()
        template_name = 'Department/showdepartmentinfo.html'
        context = {'department_obj': department_obj}
        return render(request, template_name, context)

    def post(self,request):
        department = Department.objects.filter(department_name__icontains=request.POST['search1'])
        professor = department[0].department_pro.all()
        student = department[0].department_stud.all()
        template_name = "Department/searchdepartment.html"
        context = {'department': department, 'professor': professor, 'student': student}
        return render(request, template_name, context)

class DepartmentUpdateView(View):
    def get(self, request, i):
        department = Department.objects.get(department_id=i)
        form = DepartmentModelForm(instance=department)
        template_name = 'Department/adddepartmentform.html'
        context = {'form': form}
        return render(request, template_name, context)

    def post(self, request, i):
        department = Department.objects.get(department_id=i)
        form = DepartmentModelForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect("show_department")
        template_name = 'Department/adddepartmentform.html'
        context = {'form': form}
        return render(request, template_name, context)

class DepartmentDeleteView(View):
    def get(self, request, i):
        department = Department.objects.get(department_id=i)
        department.delete()
        return redirect("show_department")

                ##################### Professor #####################

class AddProfessorView(View):
    def get(self,request):
        form = ProfessorModelForm()
        template_name = 'Professor/addprofessorform.html'
        context = {'form':form}
        return render(request, template_name, context)
    def post(self,request):
        form = ProfessorModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_professor")
        template_name = 'Professor/addprofessorform.html'
        context = {'form': form}
        return render(request, template_name, context)

class ShowProfessorView(View):
    def get(self,request):
        professor_obj = Professor.objects.all()
        template_name = 'Professor/showprofessorinfo.html'
        context = {'professor_obj': professor_obj}
        return render(request, template_name, context)

    def post(self, request):
        professor_obj = Professor.objects.filter(Professor_name__icontains=request.POST['search1'])
        template_name = "Professor/showprofessorinfo.html"
        context = {'professor_obj': professor_obj}
        return render(request, template_name, context)


class ProfessorUpdateView(View):
    def get(self, request, i):
        professor = Professor.objects.get(Professor_name=i)
        form = ProfessorModelForm(instance=professor)
        template_name = 'Professor/addprofessorform.html'
        context = {'form': form}
        return render(request, template_name, context)

    def post(self, request, i):
        professor = Professor.objects.get(Professor_name=i)
        form = ProfessorModelForm(request.POST, instance=professor)
        if form.is_valid():
            form.save()
            return redirect("show_professor")
        template_name = 'Professor/addprofessorform.html'
        context = {'form': form}
        return render(request, template_name, context)

class ProfessorDeleteView(View):
    def get(self, request, i):
        professor = Professor.objects.get(Professor_name=i)
        professor.delete()
        return redirect("show_professor")



                                 ################## Student ######################
class AddStudentView(View):
    def get(self,request):
        form = StudentModelForm()
        template_name = 'Student/addstudentform.html'
        context = {'form':form}
        return render(request, template_name, context)
    def post(self,request):
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_student")
        template_name = 'Student/addstudentform.html'
        context = {'form': form}
        return render(request, template_name, context)

class ShowStudentView(View):
    def get(self,request):
        student_obj = Student.objects.all()
        template_name = 'Student/showstudentinfo.html'
        context = {'student_obj': student_obj}
        return render(request, template_name, context)

    def post(self, request):
        student_obj = Student.objects.filter(name__icontains=request.POST['search1'])
        template_name = "Student/showstudentinfo.html"
        context = {'student_obj': student_obj}
        return render(request, template_name, context)


class StudentUpdateView(View):
    def get(self, request, i):
        student_obj = Student.objects.get(roll_no=i)
        form = StudentModelForm(instance=student_obj)
        template_name = 'Student/addstudentform.html'
        context = {'form': form}
        return render(request, template_name, context)

    def post(self, request, i):
        student_obj = Student.objects.get(roll_no=i)
        form = StudentModelForm(request.POST, instance=student_obj)
        if form.is_valid():
            form.save()
            return redirect("show_student")
        template_name = 'Student/addstudentform.html'
        context = {'form': form}
        return render(request, template_name, context)

class StudentDeleteView(View):
    def get(self, request, i):
        student_obj = Student.objects.get(roll_no=i)
        student_obj.delete()
        return redirect("show_student")

