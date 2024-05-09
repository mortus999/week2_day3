
#Tuples


# Task 1: Formatting Flight Itineraries
# Create a Python function that takes a list of tuples as an argument.
# Each tuple contains information about a flight itinerary: (traveler_name, origin, destination).
# The function should format and return a string that lists each itinerary.
# For example, if the input is [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")],
#  the output should be a string formatted as:
# "Itinerary 1: Alice - From New York to London
#  Itinerary 2: Bob - From Tokyo to San Francisco"

flight_log = ("soap","Indiana","mexico"), ("price","South America","Berlin")
def flight_itn(flight):
    for index, flight in enumerate(flight):
        print(f'Itinerary {index + 1}: {flight[0]} - From {flight[1]} to {flight[2]}')
flight_itn(flight_log)


# Task 1: Library System Enhancement
# Sharpen your skills in managing and modifying data within tuples and lists.

library_books = [("1984","George Orwell"), ("brave new world", "Aldous Huxley")]
def library_system(library):
    for book, title in library_books:
        if library[0] == book:
            print("that book already in the library")
            return library_books
        
    library_books.append(library)
    return library_books

print(library_system(("Ulysses", "James Joyce")))
print(library_system(("The Great Gatsby", "F. Scott Fitzgerald")))
print(library_system(("Ulysses", "James Joyce")))



# Task 1: Customer Order Processing Refine your skills in tuple unpacking by managing customer orders.
# Problem Statement: You are given a list of tuples, each representing a customer's order. Each tuple contains the customer's name, the product ordered
# , and the quantity. Your task is to unpack each tuple and print the order details in a user-friendly format.
order = [
    ("Alice.","Laptop", 1),
    ("Bob", "Camera", 2),
    ("Susie", "Stapler", 5),
    ("Dillon", "Paper Shredder", 1)
]
for name, item, quantity in order:
    print(f"{name} placed an order. It was for a {item} and the quantity was {quantity}.")




