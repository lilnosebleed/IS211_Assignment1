class Book:
    def __init__(self, author="", title=""):
        self.author = author
        self.title = title
    
    def display(self):
        print(self.title + ", written by " + self.author)


if __name__ == "__main__":
    book1 = Book("J.k. rowling", "Harry Potter and the Goblet of Fire")
    book2 = Book("Walter Scott", "Ivanhoe: A Romance")
    book1.dispaly()
    book2.display()