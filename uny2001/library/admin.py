from django.contrib import admin

from .models import Author, Student, Book, BookAuthors, BookStudent

admin.site.register(Author)
admin.site.register(Student)
admin.site.register(Book)
admin.site.register(BookAuthors)
admin.site.register(BookStudent)

admin.site.site_header = "Библиотека"
