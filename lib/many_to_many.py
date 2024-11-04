class Author:
    all = []
    
    def __init__(self, name):
        self.name = name
        self.contracts_list = []
        Author.all.append(self)
    
    def contracts(self):
        return self.contracts_list
    
    def books(self):
        return list({contract.book for contract in self.contracts_list})
    
    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        self.contracts_list.append(contract)
        return contract
    
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts_list)


class Book:
    all = []
    
    def __init__(self, title):
        self.title = title
        self.contracts_list = []
        Book.all.append(self)
    
    def contracts(self):
        return self.contracts_list
    
    def authors(self):
        return list({contract.author for contract in self.contracts_list})


class Contract:
    all = []
    
    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Invalid author, must be an instance of Author class")
        if not isinstance(book, Book):
            raise Exception("Invalid book, must be an instance of Book class")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
        
        # Automatically add this contract to both the author's and book's contracts lists
        author.contracts_list.append(self)
        book.contracts_list.append(self)
    
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
