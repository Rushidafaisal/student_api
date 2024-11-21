from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    email=models.EmailField(unique=True)
    enrollment_date=models.DateField(auto_now_add=True)

    class Meta:
        db_table='student_tb'