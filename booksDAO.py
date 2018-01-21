import pymongo

class Books:

    def __init__(self, db):
        self.db = db
        self.books = self.db.books
    
    def  get_n_books(self):
        """
        Temporarily this function simply return all books
        present os the books collection
        """

        books = None
        try:
            books = self.books.count()
        except:
            print('Erro ao buscar estante')
        
        if books is None:
            print('Ainda nao ha livros na base')
            return 0

        return books

    def add_books(self, title, author, year):

        book = {
            'title': title,
            'author': author,
            'year': year
        }

        try:
            self.books.insert_one(book)
            return True
        except:
            print('Livro nao adicionado')
            return False