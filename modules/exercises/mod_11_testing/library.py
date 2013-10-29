from time import sleep


class ConnectionError(Exception):
    pass


class MyConnection(object):

    def __init__(self, host, port):
        print "init connection to database"

    def get_book(self, book_id):
        if book_id <= 0:
            raise ConnectionError('Invalid book_id')
        print "Getting elements for id {}".format(id)
        if book_id == 34:
            return {"book_id": "34", "author_name": "J.R.R Tolkien", "name": "El hobbit"}
        return None

    def get_author(self, author_name):
        print "Getting author for name".format(author_name)
        sleep(1)
        if author_name == "J.R.R Tolkien":
            return {"name": "J.R.R Tolkien", "age": 50, "best_sellers": 5}
        return None
