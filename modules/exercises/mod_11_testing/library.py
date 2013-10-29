from time import sleep


class ConnectionError(Exception):
    """Internal Exception raised when a problem happens
    """
    pass


class MyConnection(object):
    """
    Fake class to simulate a database access class. It can be used
    to ilustrate the use of mocking.
    """

    def __init__(self, host, port):
        print "init connection to database"

    def get_book(self, book_id):
        """
        Fake the typical get operation in database of querying a single object.
        We perform a get over a book collection/table.
        Only book_id=34 will return something, otherwise None result.
        :returns a valid dict with book data as if it's were stored in database.
        :raise ConnectionError if book_id is negative
        """
        if book_id <= 0:
            raise ConnectionError('Invalid book_id')
        print "Getting elements for id {}".format(book_id)
        if book_id == 34:
            return {"book_id": "34", "author_name": "J.R.R Tolkien", "name": "El hobbit"}
        return None

    def get_author(self, author_name):
        """
        Fake the typical get operation in database of querying a single object.
        We perform the query against a author collection/table.
        An sleep is done to ilustrate a computationally expensive operation. 
        :returns a valid dict with author data or None
        """
        print "Getting author {}".format(author_name)
        sleep(1)
        if author_name == "J.R.R Tolkien":
            return {"name": "J.R.R Tolkien", "age": 50, "best_sellers": 5}
        return None
