from django.db import models

class Student(models.Model):
    STUDENT_STATUS_CHOICES = [
        ('ER', 'Enrolled'),
        ('SP', 'Suspended'),
        ('GD', 'Graduated'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    date_of_birth = models.DateField()
    status = models.CharField(max_length=10, choices=STUDENT_STATUS_CHOICES, default='ER')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    COURSE_LEVEL_CHOICES = [
        ('BE', 'Beginner'),
        ('IN', 'Intermediate'),
        ('AD', 'Advanced'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    instructor = models.ForeignKey('Instructor', on_delete=models.CASCADE, default=1)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    level = models.CharField(max_length=10, choices=COURSE_LEVEL_CHOICES)

    def __str__(self):
        return self.title

class Instructor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField()
    courses_taught = models.ManyToManyField(Course, related_name='instructors', blank=True)
    students_taught = models.ManyToManyField(Student, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

