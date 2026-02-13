from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from django.contrib import messages
from .forms import StudentForm, RegisterForm
from django.contrib.auth import login, logout , authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer
from django.db.models import Count


@login_required
def student_list(request):
    students = Student.objects.all()
    paginator = Paginator(students , 5)
    page_number= request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    search_query= request.GET.get('search')
    if search_query:
        students = students.filter(name__icontains = search_query) 
    return render(request, 'list.html', 
                  {
                      'students': students,
                      'page_obj' : page_obj
                  })


@login_required
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "student added")
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'add.html', {'form': form})

@login_required
def edit_student(request, id):
    if not request.user.is_superuser:
        return HttpResponse("only admin can edits student")
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES , instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "student updated")
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'edit.html', {
        'form': form ,
        'student': student
        })

@login_required
def delete_student(request, id):
    if not request.user.is_superuser:
        return HttpResponse("only admin can delete student")
    student = get_object_or_404(Student, id=id)
    student.delete()
    messages.success(request, "student deleted")
    return redirect('student_list')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user= form.save(commit = False)
            user.set_password(form.cleaned_data['password'])
            user.save()
        return redirect('user_login')
    else:
            form = RegisterForm()
    return render(request, 'register.html', {'form' : form})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = username, password= password)
        if user is not None:
            login(request, user)
            return redirect('student_list')
        else:
            return render(request, "login.html", {"error" : "invalid username and password"})
    return render(request, "login.html")  

def user_logout(request):
    logout(request)
    return redirect('user_login')

@api_view(['GET', 'POST'])
def student_api(request):

    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def student_detail_api(request, id):

    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    if request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@login_required
def dashboard(request):
    total_students = Student.objects.count()
    passed_students = Student.objects.filter(marks__gte=35).count()
    failed_students = Student.objects.filter(marks__lt=35).count()
    context = {
        'total_students' : total_students,
        'passed_students' : passed_students,
        'failed_students' : failed_students,
    }
    return render(request, 'dashboard.html' , context)
