from django.urls import include, path
from . import views

urlpatterns = [
    path('add_student', views.student_add, name='add_student'),
    path('students', views.students_list, name='students_list'),
    path('edit_student', views.student_edit, name='edit_student'),
    path('student', views.student_details, name='student_details'),
]
