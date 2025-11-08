from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=120, verbose_name="Student Name")
    email = models.EmailField(max_length=287, verbose_name="Student Email")

    def __str__(self):
        return str(self.id)


class Teacher(models.Model):
	tname = models.CharField(max_length=200, verbose_name="Teacher Name")
	taddress = models.CharField(max_length=300,verbose_name="Teacher Address")
	subject = models.CharField(max_length=200,verbose_name="Teacher Subject")
	classrom = models.CharField(max_length=200,verbose_name="Teacher Classroom")

	def __str__(self):
		 return str(self.id)