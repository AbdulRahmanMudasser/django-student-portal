from django.contrib import messages
from django.shortcuts import render

from student.models import Parent, Student

# Add Student View
def student_add(request):
    # Check if Request Method is POST
    if request.method == 'POST':
        # Grab Student Information
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        student_id = request.POST.get('student_id')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        student_class = request.POST.get('student_class')
        religion = request.POST.get('religion')
        joining_date = request.POST.get('joining_date')
        phone = request.POST.get('mobile_number')
        admission_id = request.POST.get('admission_number')
        student_section = request.POST.get('section')
        image = request.FILES.get('student_image')
        
        # Grab Student's Parent Information
        father_name = request.POST.get('father_name')
        father_occupation = request.POST.get('father_occupation')
        father_phone = request.POST.get('father_mobile')
        father_email = request.POST.get('father_email')
        mother_name = request.POST.get('mother_name')
        mother_occupation = request.POST.get('mother_occupation')
        mother_phone = request.POST.get('mother_mobile')
        mother_email = request.POST.get('mother_email')
        present_address = request.POST.get('present_address')
        permanent_address = request.POST.get('permanent_address')
        
        # Save Student's Parent Information
        parent = Parent.objects.create(
            father_name = father_name, 
            father_occupation = father_occupation, 
            father_phone = father_phone, 
            father_email = father_email, 
            mother_name = mother_name, 
            mother_occupation = mother_occupation, 
            mother_phone = mother_phone, 
            mother_email = mother_email, 
            present_address = present_address, 
            permanent_address = permanent_address
        )
        
        # Save Student Information
        student = Student.objects.create(
            first_name = first_name,
            last_name = last_name,
            student_id = student_id,
            gender = gender,
            date_of_birth = date_of_birth,
            student_class = student_class,
            religion = religion,
            joining_date = joining_date,
            phone = phone,
            admission_id = admission_id,
            student_section = student_section,
            image = image,
            parent = parent,
        )       
        
        # Show Success Message
        messages.show(request, "Student Added Successfully")
        
        # Render Student List Template
        render(request, 'students/students.html')
    
    # Render Add Student Template
    return render(request, 'students/add-student.html')

# All Student Details View
def students_list(request):
    # Grab Student Information from Database
    students_list = Student.objects.select_related('parent')
    
    context = {
        'students_list': students_list,
    }
    
    # Render Student Details Template
    return render(request, 'students/students.html', context)

# Edit Student View
def student_edit(request):
    # Render Edit Student Template
    return render(request, 'students/edit_student.html')

# Student Details View
def student_details(request):
    # Render Student Details Template
    return render(request, 'students/student-details.html')
