from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header="USAP LIBRARY MANAGEMENT SYSTEM"

def returned_borrowed_book(modeladmin, request, queryset):
    queryset.update(has_returned= True)
    for book in queryset:
        book.book.quantity= book.book.quantinty+1
        book.book.save()
returned_borrowed_book.short_description= ("Update returned books")
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("firstname","lastname","grade","email")
    list_filter = ("grade",)
    search_fields = ("firstname","lastname","email",)

@admin.register(Librarian)
class LibrarianAdmin(admin. ModelAdmin):
    list_display = ("firstname","lastname","date_joined")
    search_fields = ("firstname","lastname",)

@admin.register(Borrowing)
class BorrowingAdmin(admin.ModelAdmin):
    list_display = ("book","student","date_borrowed","has_returned","due_date",)
    list_filter = ("has_returned",)
    actions=[returned_borrowed_book]
   
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title","author","date_published")
    search_fields = ("title","author",)



