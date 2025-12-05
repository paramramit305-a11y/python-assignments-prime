# Q2. Create a class Book with the following attributes:

#  -> title
#  -> author
#  -> list of reviews

# And add methods to:

#  -> Add a new review
#  -> count reviews
#  -> display all reviews 

class Book:
    def __init__(self, title, author, list_of_reviews):
        self.title = title
        self.author = author
        self.reviews = []

    def add_reviews(self, reviews):
        self.reviews.append(reviews)

    def count_reviews(self):
        print(len(self.reviews))

    def display_reviews(self):
        for reviews in self.reviews:
            print(reviews)

    def __str__(self):
        return f"{self.title} written by {self.author}"

b1 = Book("Harryb potter", "Jk Rowling", [])
b1.add_reviews("Great")
b1.count_reviews()
b1.display_reviews()
print(b1)