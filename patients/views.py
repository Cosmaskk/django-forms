from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .forms import StudentForm
from patients.models import Student


# Create your views here.
def employee_form(request):
    form = employee_form
    return render(request, 'employee_form.html', {'form':form})
def employee_list(request, id=0):
    if request.method == 'GET':
        if id ==0:
           form = StudentForm()
        else:
            employee = Student.objects.get(pk=id)
            form = StudentForm(instance=employee)
        return render(request, 'employee_list.html', {'form': form})
    else:
        if id==0:
            form = StudentForm(request.POST)
            form.save()
        else:
            employee = Student.objects.get(pk=id)
            form = StudentForm(request.POST, instance=employee)
            if form.is_valid():
                form.save()
        return redirect('/patients/show/')


def show(request):
    context = {'show': Student.objects.all()}
    return render(request, 'show.html',context)

def delete(request,id):
    employee = Student.objects.get(pk=id)
    employee.delete()
    return redirect('/patients/show/')