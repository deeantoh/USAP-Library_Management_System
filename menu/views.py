from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from menu.models import Book, Borrowing, Student
# Create your views here.


@login_required(login_url="login")
def home(request):
    if request.user.is_staff:
        return redirect("admin:index")
    print(request.user)
    return render(request,'base.html')

def view_all_books(request):
    books = Book.objects.all()
    return render(request,'books.html',{'books':books})

def student_booking(request,book_id):
    book = Book.objects.get(id = book_id)
    email = request.user.email
    student = Student.objects.get(email = email)
    if student.students_borrowings.filter(has_returned= False).exists():
        messages.error(request,"You have to return borrowed books first!")
        return redirect("menu:view_books")
    else:
        Borrowing.objects.create(
            book = book,
            student = student
        )
        book.quantity = book.quantity - 1
        book.save()

    return redirect("menu:borrowings")

def view_borowings(request):
    email = request.user.email
    student = Student.objects.get(email = email)
    borrowings = Borrowing.objects.filter(student = student)
    return render(request,'borrowings.html',{'borrowings':borrowings})


