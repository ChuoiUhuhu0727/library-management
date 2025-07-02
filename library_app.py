import streamlit as st
from library_core import Library, Librarian, Member

# Sample data for demonstration
books_data = [
    {"title": "1984", "author": "George Orwell", "isbn": "12345"},
    {"title": "Python OOP", "author": "Jane Smith", "isbn": "54321"},
    {"title": "Clean Code", "author": "Robert C. Martin", "isbn": "11122"}
]
members_data = [
    {"name": "Alice", "member_type": "regular"},
    {"name": "Bob", "member_type": "premium"}
]

library = Library(books_data, members_data)

def main():
    st.title("Library Management System")
    role = st.selectbox("Select your role", ["librarian", "regular", "premium"])

    if role == "librarian":
        lib_action = st.selectbox("Select action", ["add", "remove"])
        librarian = Librarian(library)
        title = st.text_input("Book Title")

        if lib_action == "add":
            author = st.text_input("Book Author")
            isbn = st.text_input("Book ISBN")
            if st.button("Add Book"):
                if title and author and isbn:
                    librarian.add_book(title, author, isbn)
                    st.success(f'Book "{title}" added successfully!')
                else:
                    st.warning("Please fill all fields.")
        elif lib_action == "remove":
            if st.button("Remove Book"):
                if title:
                    try:
                        librarian.remove_book(title)
                        st.success(f'Book "{title}" removed successfully (if it existed)!')
                    except ValueError as ve:
                        st.warning(str(ve))
                else:
                    st.warning("Please enter the book title to remove.")

        st.subheader("Current Books")
        for book in library.books_data:
            st.write(f"- {book.title} by {book.author} (ISBN: {book.isbn})")
        return

    # For members
    name = st.selectbox("Select your name", [m["name"] for m in members_data])
    member_obj = library.check_name(name)
    action = st.selectbox("Select action", ["borrow", "return"])
    book_title = st.selectbox("Select book", [book.title for book in library.books_data])

    if st.button("Submit"):
        try:
            library.check_action(action)
            result = library.check_book(member_obj, action, book_title)
            st.success(result)
        except Exception as e:
            st.error(str(e))

    st.subheader("Your borrowed books:")
    st.write(", ".join(member_obj.books) if member_obj.books else "None")

if __name__ == "__main__":
    main()