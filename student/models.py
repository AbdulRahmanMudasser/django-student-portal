from django.db import models
from django.utils.text import slugify

# Parent Model
class Parent(models.Model):
    father_name = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=100)
    father_phone = models.CharField(max_length=15)
    father_email = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    mother_email = models.CharField(max_length=100)
    mother_phone = models.CharField(max_length=15)
    present_address = models.TextField()
    permanent_address = models.TextField()
    
    def __str__(self):
        return f"{self.father_name} & {self.mother_name}"

# Student Model
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')])
    date_of_birth = models.DateField()
    student_class = models.CharField(max_length=100)
    religion = models.CharField(max_length=20)
    joining_date = models.DateField()
    phone = models.CharField(max_length=15)
    admission_id = models.CharField(max_length=15)
    student_section = models.CharField(max_length=15)
    image = models.ImageField(upload_to='student/', blank=True)
    parent = models.OneToOneField(Parent, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.first_name}-{self.last_name}-{self.student_id}")
        super(Student, self).save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_id})"
    