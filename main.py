# main.py

import streamlit as st
from book_manager import add_book, remove_book, search_books, display_books
from statistics import calculate_stats, average_rating # type: ignore

st.title("📚 Personal Library Manager")

if 'library' not in st.session_state:
    st.session_state.library = []

menu = st.sidebar.radio("Menu", [
    "Add a Book", "Remove a Book", "Search for a Book", "Display All Books", "Display Statistics"
])

# Add a Book
if menu == "Add a Book":
    st.header("📖 Add a Book")
    title = st.text_input("Enter the book title:")
    author = st.text_input("Enter the author:")
    year = st.number_input("Enter the publication year:", min_value=0, max_value=9999, step=1)
    genre = st.text_input("Enter the genre:")
    read_status = st.selectbox("Have you read this book?", ["Yes", "No"])
    rating = None
    if read_status == "Yes":
        rating = st.slider("Rate this book (1 to 5 stars)", 1, 5)

    if st.button("Add Book"):
        add_book(st.session_state.library, title, author, year, genre, read_status == "Yes", rating)
        st.success("Book added successfully!")

# Remove a Book
elif menu == "Remove a Book":
    st.header("🗑️ Remove a Book")
    titles = [book["title"] for book in st.session_state.library]
    if titles:
        selected_title = st.selectbox("Select a book to remove:", titles)
        if st.button("Remove"):
            st.session_state.library = remove_book(st.session_state.library, selected_title)
            st.success("Book removed successfully!")
    else:
        st.info("Library is empty.")

# Search for a Book
elif menu == "Search for a Book":
    st.header("🔍 Search for a Book")
    search_by = st.radio("Search by:", ["Title", "Author"])
    query = st.text_input("Enter your search:")
    if query:
        results = search_books(st.session_state.library, search_by, query)
        if results:
            for book in display_books(results):
                st.write(book)
        else:
            st.warning("No matching books found.")

# Display All Books
elif menu == "Display All Books":
    st.header("📚 Your Library")
    if st.session_state.library:
        for book in display_books(st.session_state.library):
            st.write(book)
    else:
        st.info("Library is empty.")

# Display Statistics
elif menu == "Display Statistics":
    st.header("📊 Library Statistics")
    total, read_count, percent = calculate_stats(st.session_state.library)
    st.write(f"**Total books:** {total}")
    st.write(f"**Books read:** {read_count}")
    st.write(f"**Percentage read:** {percent:.2f}%")

    avg_rating = average_rating(st.session_state.library)
    if avg_rating:
        st.write(f"**Average rating of read books:** ⭐ {avg_rating:.2f}/5")
