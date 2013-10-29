from mod_11_testing.library import MyConnection
from mod_11_testing.library import ConnectionError
import logging

logger = logging.getLogger(__name__)


class GetBookAuthor(object):
    """
    Process queries in database using library to return a formatted output
    combining results of some queries.
    """

    def __init__(self):
        # sleep(1) ilustrate the sleep mocking maybe
        self.db = MyConnection(None, None)

    def get_info(self, book_id):
        """
        Return an object with combined information of book/author.
        Empty result is available.
        :param books_id book_id to recover from db
        :return dict with databa combined
        :raise Exception if database can not be connected
        """
        try:
            book_data = self.db.get_book(book_id)
            author = self.db.get_author(book_data['author_name'])
            return {'title': book_data['name'], "author_name": book_data['author_name'],
                    'best_sellers': author['best_sellers']}
        except ConnectionError as e:
            logger.info(str(e))
            logger.error("Conection with database lost")
            raise Exception('no connection')

    def get_info_list(self, *books_id):
        """
        Return an array with combined information of book/author.
        Empty result is available.
        :param books_id variable arguments of book_id to recover from db
        :return list with data combined
        """
        output = []
        try:
            for book_id in books_id:
                book_data = self.db.get_book(book_id)
                author = self.db.get_author(book_data['author_name'])
                output.append({'title': book_data['name'], "author_name": book_data['author_name'],
                'best_sellers': author['best_sellers']})
        except ConnectionError as e:  # skipping
            logger.error("Conection with database lost")
            logger.info(str(e))
            return []

        return output
