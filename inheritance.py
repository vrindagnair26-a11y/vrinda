class Publisher:
    def __init__(self, publisher):
        self.publisher = publisher

    def display(self):
        print("Publisher:", self.publisher)


class Book(Publisher):
    def __init__(self, publisher, title, author):
        super().__init__(publisher)
        self.title = title
        self.author = author

    def display(self):
        print("Book Title:", self.title)
        print("Author:", self.author)


class Python(Book):
    def __init__(self, publisher, title, author, price):
        super().__init__(publisher, title, author)
        self.price = price

    def display(self):
        super().display()
        print("Publisher:", self.publisher)
        print("Price: Rs.", self.price)


# Creating an object using constructor invocation
p = Python("ABC Publications", "Python Programming",
           "John Smith", 450)

# Displaying book information
p.display()