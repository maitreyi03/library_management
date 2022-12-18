#custom exceptions to raise

class BookNotFound(Exception):
    """Raised while looking for a book when not in library."""
    pass


class BookIDExists(Exception):
    """Raised while adding a book of an already existing book id."""
    pass


class NotANumSentences(Exception):
    pass
