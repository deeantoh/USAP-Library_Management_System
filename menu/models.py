from django.db import models
import datetime

# Create your models here.
grades =(
    ("Lower 6", "Lower 6"),("Upper 6", "Upper 6")
)
class Student(models.Model):
    firstname= models.CharField(max_length=20)
    lastname= models.CharField(max_length=20)
    grade= models.CharField(max_length=20, choices=grades)
    email = models.EmailField(max_length=100)

    def __str__(self) -> str:
        return self.firstname + " " + self.lastname

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date_published = models.DateField()
    quantity = models.IntegerField(null=True,blank=True)

    def __str__(self) -> str:
        return self.title


class Librarian(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    date_joined = models.DateField()


class Borrowing(models.Model):
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING, related_name="book_borrowings")
    student = models.ForeignKey(Student,on_delete=models.DO_NOTHING,related_name='students_borrowings')
    date_borrowed = models.DateField(auto_now_add=True)
    has_returned = models.BooleanField(default=False)
    due_date = models.DateField(null=True,blank=True)

    @property
    def is_due(self):
        # if current date is greater than due and book is not yet returned
        # TODO
        if datetime.datetime.today().date() > self.due_date and self.has_returned == False :
            # freeze student account
            # TODO
            pass
    
    
    @property
    def send_notification(self):
        today_date = datetime.datetime.today().date()
        if self.due_date - today_date == 1 and self.has_returned == False:
            # Send email to student
            student_email = self.student.email
            # send_email(student_email)
            pass

