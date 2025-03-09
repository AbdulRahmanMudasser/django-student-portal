from django.contrib import admin
from . import models

# Register Parent Model
@admin.register(models.Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('father_name', 'mother_name', 'father_phone', 'mother_phone',)
    search_fields = ('father_name', 'mother_name', 'father_phone', 'mother_phone',)
    list_filter = ('father_name', 'mother_name',)
    
# Register Student Model
@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'student_id', 'gender', 'date_of_birth', 'student_class', 'joining_date', 'phone', 'admission_id', 'student_section',)
    search_fields = ('first_name', 'last_name', 'student_id', 'student_class', 'admission_id',)
    list_filter = ('gender', 'student_class', 'student_section',)
    readonly_fields = ('image',)
