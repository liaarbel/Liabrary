from app import app
from app import models

if __name__ == '__main__':
    models.User.create_table(fail_silently=True)
    models.Author.create_table(fail_silently=True)
    models.Book.create_table(fail_silently=True)
    models.BorrowBooks.create_table(fail_silently=True)
    app.run(threaded=True, port=5000)
