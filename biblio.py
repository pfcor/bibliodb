import pymongo, bottle
import booksDAO

__author__ = 'pfcor'

@bottle.route('/')
def biblio_main():

    cookie = bottle.request.get_cookie("session")

    # username = sessions.get_username(cookie)
    username='teste'
    # todo: this is not yet implemented at this point in the course

    return bottle.template('biblio_template')#, dict(username=username))


@bottle.get('/n_books')
def present_books():

    n_books = books.get_n_books()

    return bottle.template('biblio_bookcount', dict(n_books=n_books))


@bottle.get('/addbook')
def present_book_adding():
    return bottle.template("biblio_addbooks",
                           dict(title="", author="",
                                year=""))

@bottle.post('/addbook')
def process_book_adding():

    title = bottle.request.forms.get("title")
    author = bottle.request.forms.get("author")
    year = int(bottle.request.forms.get("year"))

    addition = books.add_books(title, author, year)
    bottle.redirect("/bookadded")

@bottle.get('/bookadded')
def present_book_added():
    return bottle.template('biblio_bookadded')





connection_string = "mongodb://localhost"
connection = pymongo.MongoClient(connection_string)
db = connection.biblio
books = booksDAO.Books(db)

bottle.run(host='127.0.0.1', port=8083)


"""

@bottle.get('/books')
def list_books():
    return bottle.template("books",
                           dict(username="", password="",
                                password_error="",
                                email="", username_error="", email_error="",
                                verify_error =""))

"""
