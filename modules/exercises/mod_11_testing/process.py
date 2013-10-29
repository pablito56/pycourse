from mod_11_testing.library import MyConnection
from mod_11_testing.library import ConnectionError
import logging

logger = logging.getLogger(__name__)


class GetBookAuthor(object):

    def __init__(self):
        self.db = MyConnection(None, None)

    def get_info(self, book_id):
        try:
            book_data = self.db.get_book(book_id)
            author = self.db.get_author(book_data['author_name'])
            return {'title': book_data['name'], "author_name": book_data['author_name'],
                    'best_sellers': author['best_sellers']}
        except ConnectionError as e:
            logger.info(str(e))
            logger.error("Conection with database lost")
            raise e

    def get_info_list(self, *books_id):
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
