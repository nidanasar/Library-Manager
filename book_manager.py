#add/remove/search books

def add_book(library,title,author,year,genre,read,rating):
    book={
        "title": title,
        "author": author,   
        "year": year,
        "genre": genre,
        "read": read,
        "rating": rating if read else None
    }
    library.append(book)

#remove book
def remove_book(library,title):
    for book in library:
        if book["title"] == title:
            library.remove(book)
            return True
    return False

#search book
def search_books(library, search_by, query):
    results = []
    for book in library:
        if (search_by == "Title" and query.lower() in book["title"].lower()) or \
           (search_by == "Author" and query.lower() in book["author"].lower()):
            results.append(book)
    return results

#display books
def display_books(library):
    result = []
    for i, book in enumerate(library, 1):
        stars = f"⭐ {book['rating']}/5" if book["read"] and book["rating"] else "No rating"
        result.append(
            f"{i}. {book['title']} by {book['author']} ({book['year']}) - "
            f"{book['genre']} - {'Read' if book['read'] else 'Unread'} - {stars}"
        )
    return result