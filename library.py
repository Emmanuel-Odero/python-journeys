class Books:
    def __init__(self, title, author, pages, edition):
        self.title = title
        self.author = author
        self.pages = pages
        self.edition = edition

book1 = Books("The Beginning of the End","Jose Curruilo", 45, "5th Edition")
book2 = Books("Love and War", "Mark Twein", 700, "11th Edition")

print(book2.title)
