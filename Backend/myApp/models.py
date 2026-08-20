from django.db import models



class Department(models.Model):
    department = models.CharField(max_length=200)
    def __str__(self):
        return self.department
    

    
class Course(models.Model):
    course = models.CharField(max_length=100)
    department = models.ManyToManyField(Department)
    def __str__(self):
        return self.course
    


class RegisterationForm(models.Model):
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.CharField(max_length=100)
    number = models.IntegerField()
    dob = models.DateField()
    address = models.CharField()
    gender = models.CharField()
    nationality = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add =True)