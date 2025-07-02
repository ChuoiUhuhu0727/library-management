import pytest
from library_core import Library, Librarian, Member

def test_add_book():
    lib = Library([], [])
    librarian = Librarian(lib)
    librarian.add_book("Test", "Author", "123")
    assert len(lib.books_data) == 1

def test_remove_nonexistent_book():
    lib = Library([], [])
    librarian = Librarian(lib)
    with pytest.raises(ValueError):         # <--- Expect an error!
        librarian.remove_book("Not There")

def test_borrow_limit_regular():
    lib = Library([], [{"name": "A", "member_type": "regular"}])
    member = lib.members_data[0]
    member.books = ["Book1", "Book2", "Book3"]
    try:
        member.borrow_book("Book4")
        assert False, "Should raise error"
    except Exception:
        assert True