from django.urls import path

from menu import views


app_name = 'menu'

urlpatterns =[
    path('', views.home, name="dashboard"),
    path('books',views.view_all_books,name="view_books"),
    path('booking/<int:book_id>/',views.student_booking,name="book"),
    path('borrowings',views.view_borowings,name="borrowings"),
]