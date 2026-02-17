from django.shortcuts import render, get_object_or_404, redirect
from students.models import Student
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count


def portal_home(request):
    students = Student.objects.all().order_by('-marks')  # highest to lowest

    total_students = students.count()
    passed_students = students.filter(marks__gte=35).count()
    failed_students = students.filter(marks__lt=35).count()

    return render(request, 'student_portal/index.html', {
        'students': students,
        'total_students': total_students,
        'passed_students': passed_students,
        'failed_students': failed_students,
    })



def portal_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'student_portal/detail.html', {
        'student': student
    })

def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.is_superuser or user.is_staff:
                return redirect("/students/")
            else:
                return redirect("/portal/my-profile/")

        else:
            return render(request, "student_portal/login.html", {
                "error": "Invalid Username or Password"
            })

    return render(request, "student_portal/login.html")





@login_required
def dashboard(request):
    return redirect("student_list")

def user_logout(request):
    logout(request)
    return redirect("/portal/")




def admin_logout(request):
    logout(request)
    return redirect("portal_home")



@login_required
def student_profile(request):
    if request.user.is_superuser:
        return redirect("student_list")

    student = Student.objects.get(user=request.user)

    return render(request, 'student_portal/detail.html', {
    'student': student
})
