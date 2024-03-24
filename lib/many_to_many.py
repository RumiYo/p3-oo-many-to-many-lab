class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)
         
    def sign_contract(self, book, date, royalties):
        new_contract = Contract(self, book, date, royalties)
        return new_contract

    def contracts(self):
        return [contract for contract in Contract.all if self == contract.author]

    def books(self):
        return [contract.book for contract in Contract.all if self == contract.author]

    def total_royalties(self):
        each_royalties = [contract.royalties for contract in Contract.all if self == contract.author]
        total_royalties = 0
        for royalties in each_royalties:
            total_royalties += royalties
        return total_royalties


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if self == contract.book]

    def authors(self):
        return [contract.author for contract in Contract.all if self == contract.book]

class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    
    @property 
    def author(self):
        return self._author

    @author.setter
    def author(self, item):
        if not isinstance(item, Author):
            raise Exception("Author must be an instance of the Author class")
        self._author = item

    @property 
    def book(self):
        return self._book

    @book.setter
    def book(self, item):
        if not isinstance(item, Book):
            raise Exception("Book must be an instance of the Book class")
        self._book = item

    @property
    def date(self):  
        return self._date
    
    @date.setter
    def date(self, item):
        if not isinstance(item, str):
            raise Exception("Date must be string")
        self._date = item

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, item):
        if not isinstance(item, int):
            raise Exception("Royalties must be number")
        self._royalties = item

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
