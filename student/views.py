from django.shortcuts import render

# Add Student View
def student_add(request):
    # Render Add Student Template
    return render(request, 'students/add-student.html')

# All Student Details View
def students_list(request):
    # Render Student Details Template
    return render(request, 'students/students.html')

# Edit Student View
def student_edit(request):
    # Render Edit Student Template
    return render(request, 'students/edit_student.html')

# Student Details View
def student_details(request):
    # Render Student Details Template
    return render(request, 'students/student-details.html')
