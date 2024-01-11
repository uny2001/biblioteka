from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("book/<int:book_id>/rent", views.booking, name="booking"),
    path("book/<int:book_id>/", views.book_details, name="book"),
    path("author/<int:author_id>/", views.author_details, name="author"),
    path("student/<int:student_id>/", views.student_details, name="student"),
    path("login/", views.login, name = "login"),
    path("logout/", views.logout, name = "logout"),
    path("search/", views.search, name = "search"),
    path("book/<int:book_id>/return", views.returning, name = "returning"),
]