from django.db import models

class Student(models.Model):
    surname = models.CharField(max_length=200, verbose_name = "Фамилия")
    name = models.CharField(max_length=200, verbose_name = "Имя")
    middlename = models.CharField(max_length=200, verbose_name = "Отчество")
    birthday = models.DateField(verbose_name = "Дата Рождения")
    email = models.CharField(max_length=200, db_index = True, verbose_name = "Электронная почта")
    password = models.CharField(max_length=200, verbose_name = "Пароль")

    def __str__(self):
        return f'{self.name} {self.surname}'
    
    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"


class Author(models.Model):
    surname = models.CharField(max_length=200, verbose_name = "Фамилия")
    name = models.CharField(max_length=200, verbose_name = "Имя")
    middlename = models.CharField(max_length=200, verbose_name = "Отчество")
    birthday = models.DateField(verbose_name = "Дата рождения")

    def __str__(self):
        return f'{self.name} {self.surname}'
    
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Book(models.Model):
    name = models.CharField(max_length=400, verbose_name = "Название")
    published_date = models.DateField(verbose_name = "Дата публикации")
    pages = models.IntegerField(verbose_name = "Количество страниц")
    age_restriction = models.CharField(max_length=10, default = "0+", verbose_name = "Возрастное ограничение")
    description = models.CharField(max_length=1000, verbose_name = "Описание")
    cover_filename = models.CharField(max_length=100, verbose_name = "Имя файла с обложкой")
    isbn = models.CharField(max_length=20, verbose_name = "Международный стандартный книжный номер(ISBN)")

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


class BookAuthors(models.Model):
    book_id = models.ForeignKey(Book, db_index = True, on_delete = models.CASCADE, verbose_name = "Книга")
    author_id = models.ForeignKey(Author, db_index = True, on_delete = models.CASCADE, verbose_name = "Автор")

    def __str__(self):
        return f'{self.book_id} {self.author_id}'
    
    class Meta:
        verbose_name = "Авторы и книги"
        verbose_name_plural = "Авторы и книги"


class BookStudent(models.Model):
    book_id = models.ForeignKey(Book, db_index = True, on_delete = models.CASCADE, verbose_name = "Книга")
    student_id = models.ForeignKey(Student, db_index = True, on_delete = models.CASCADE, verbose_name = "Забронированна студентом")

    def __str__(self):
        return f'{self.book_id} {self.student_id}'

    class Meta:
        verbose_name = "Забронированные книги"
        verbose_name_plural = "Забронированные книги"
