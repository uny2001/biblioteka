from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Author, Book, Student, BookStudent, BookAuthors

def makeAuthor(book):
    author = {}
    author["name"] = book.author_id.name
    author["surname"] = book.author_id.surname
    author["initials"] = f'{book.author_id.name[0]}.{book.author_id.middlename[0]}.'
    author["id"] = book.author_id.id

    return author


def index(request):
    if 'authorized' not in request.session or not request.session['authorized']:
        return HttpResponseRedirect(reverse("login"))
    
    student_id = request.session['student_id']
    books = BookAuthors.objects.all().select_related("book_id").select_related("author_id").order_by("book_id__name")

    structured = []
    for book in books:
        if len(structured) and structured[-1:][0]["book_name"] == book.book_id.name:
            structured[-1:][0]["authors"].append(makeAuthor(book))
        else:
            current = {}
            current["book_name"] = book.book_id.name
            current["cover_filename"] = book.book_id.cover_filename
            current["isbn"] = book.book_id.isbn
            current["pages"] = book.book_id.pages
            current["book_id"] = book.book_id.id
            current["restirction"] = book.book_id.age_restriction
            current["description"] = book.book_id.description
            current["authors"] = [makeAuthor(book)]
            structured.append(current)

    return render(request, "index.html", {'books': structured, 'current_user': student_id})


def book_details(request, book_id):
    if 'authorized' not in request.session or not request.session['authorized']:
        return HttpResponseRedirect(reverse("login"))

    book = get_object_or_404(Book, pk = book_id)

    authors = None
    rented_by = None
    try:
        bookStudent = BookStudent.objects.get(book_id = book_id)
        rented_by = bookStudent.student_id
    except BookStudent.DoesNotExist:
        pass
    try:
        bookAuthors = list(BookAuthors.objects.filter(book_id = book_id).values_list('author_id', flat=True))
        authors = Author.objects.filter(id__in = bookAuthors)
    except BookAuthors.DoesNotExist:
        pass

    return render(request, "book.html", {'book': book, "rented_by": rented_by, "authors": authors})


def author_details(request, author_id):
    if 'authorized' not in request.session or not request.session['authorized']:
        return HttpResponseRedirect(reverse("login"))
    
    author = get_object_or_404(Author, pk = author_id)
    try:
        book_ids = BookAuthors.objects.filter(author_id = author_id).values_list('book_id', flat=True)
        books = Book.objects.filter(id__in = book_ids)
    except BookAuthors.DoesNotExist:
        books = None

    return render(request, "author.html", {'author': author, 'books': books})


def student_details(request, student_id):
    if 'authorized' not in request.session or not request.session['authorized']:
        return HttpResponseRedirect(reverse("login"))

    student = get_object_or_404(Student, pk = student_id)
    try:
        book_ids = BookStudent.objects.filter(student_id = student_id).values_list('book_id', flat=True)
        books = Book.objects.filter(id__in = book_ids)
    except BookAuthors.DoesNotExist:
        books = None
    return render(request, "student.html", {'student': student, 'books': books})


def booking(request, book_id):
    if 'authorized' not in request.session or not request.session['authorized']:
        return HttpResponseRedirect(reverse("login"))
    
    student_id = request.session["student_id"]
    book = get_object_or_404(Book, pk = book_id)
    student = get_object_or_404(Student, pk = student_id)
    BookStudent.objects.create(student_id = student, book_id = book)

    return HttpResponseRedirect(reverse(f"book", args=[book.id]))

def login(request):
    if request.method != 'POST':
        return render(request, "login.html")

    if not request.POST or 'email' not in request.POST or 'password' not in request.POST:
        return HttpResponseBadRequest('Отсутсвует необходимая информация')

    email = request.POST.get('email','')
    password = request.POST.get('password','')
    try:
        student = Student.objects.get(email = email )
        if student.password == password:
            request.session.set_expiry(86400)
            request.session['student_id'] = student.id
            request.session['student_name'] = f'{student.name} {student.surname}'
            request.session['authorized'] = True
            return HttpResponseRedirect(reverse("index"))
    except Student.DoesNotExist:
        return HttpResponseForbidden("Неверный email или пароль")
    

def logout(request):
    request.session['authorized'] = False
    if 'student_id' in request.session:
        del(request.session['student_id'])
    if 'student_name' in request.session:
        del(request.session['student_name'])
    return render(request, "logout.html")


def returning(request, book_id):
    if 'authorized' not in request.session or not request.session['authorized']:
        return HttpResponseRedirect(reverse("login"))
    
    student_id = request.session["student_id"]
    try:
        BookStudent.objects.get(book_id = book_id, student_id = student_id).delete()
    except:
        pass

    return HttpResponseRedirect(reverse(f"book", args=[book_id]))


def search(request):
    return HttpResponse("В разработке")