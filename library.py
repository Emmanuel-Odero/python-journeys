class Books:
    def __init__(self, title, author, pages, edition):
        self.title = title
        self.author = author
        self.pages = pages
        self.edition = edition

book1 = Books("The Beginning of the End")
book2 = Books("Love and War")

print(book2.title)
