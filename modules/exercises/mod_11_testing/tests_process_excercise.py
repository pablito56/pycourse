from process import GetBookAuthor
import unittest
from mock import MagicMock, patch, ANY, call


class TestMyDatabaseAccess(unittest.TestCase):
    """
    """

    def setUp(self):
        """setUp is executed BEFORE each test
        """
        # Mock database
        self.mock_db_instance = MagicMock(name='connection_mock')

        # The target should be the complete module path...
        self.patcher = patch('modules.exercises.mod_11_testing.process.MyConnection')
        self.mock_db = self.patcher.start()
        # We have patched the import, not the constructor, MagicMock returns a magicMock
        self.mock_db.return_value = self.mock_db_instance

    def tearDown(self):
        try:
            self.patcher.stop()
        except RuntimeError:  # because is an example only, this is against ZEN of python
            pass

    # Some nosetests versions require 'test' to appear in the function name
    def test_get_valid_id(self):
        """
        """
        # use return value
        self.mock_db_instance.get_book.return_value = {"book_id": "1", "author_name": "test_mock", "name": "name_mock"}
        self.mock_db_instance.get_author.return_value = {"name": "name_mock", "age": -1, "best_sellers": -5}

        # call the method
        get_book = GetBookAuthor()
        data = get_book.get_info(25)

        # asserts
        self.mock_db.assert_called_once_with(None, None)  # constructor
        self.mock_db_instance.get_book.assert_called_once_with(25)
        self.mock_db_instance.get_author.assert_called_once_with(ANY)
        self.assertEquals("name_mock", data['title'])

    @patch('modules.exercises.mod_11_testing.library.sleep')
    def test_get_valid_id_not_mocking_should_not_sleep(self, sleep_mock):
        """
        """
        self.patcher.stop()

        # call the method
        get_book = GetBookAuthor()
        data = get_book.get_info(34)

        self.assertEquals("El hobbit", data['title'])
        sleep_mock.assert_called_once_with(ANY)

    def test_get_invalid_id_should_raise_exception(self):
        self.mock_db_instance.get_book.side_effect = Exception("test")
        self.mock_db_instance.get_author.return_value = {"name": "name_mock", "age": -1, "best_sellers": -5}

        get_book = GetBookAuthor()

        self.assertRaises(Exception, get_book.get_info, -1)

    # Some nosetests versions require 'test' to appear in the function name
    def test_get_valid_id_with_cm(self):
        """
        """
        # use return value
        with patch('modules.exercises.mod_11_testing.process.MyConnection') as mock_db_class:
            # return value
            mock_db = MagicMock(name='mock_db_instance')
            mock_db_class.return_value = mock_db
            mock_db.get_book.return_value = {"book_id": "10", "author_name": "test__another_mock", "name": "name_another_mock"}
            mock_db.get_author.return_value = {"name": "name_another_mock", "age": -10, "best_sellers": -50}

            # call the method
            get_book = GetBookAuthor()
            data = get_book.get_info(10)

            # asserts
            mock_db.get_book.assert_called_once_with(10)
            mock_db.get_author.assert_called_once_with(ANY)
            self.assertEquals("name_another_mock", data['title'])
            self.assertEquals(0, self.mock_db.call_count)

    def test_get_valid_id_with_patch_object(self):
        """
        """
        # call the method
        get_book = GetBookAuthor()
        # use return value
        with patch.object(get_book, 'db') as mock_db:
            # mock_db is already our mock, no import mock this time
            mock_db.get_book.return_value = {"book_id": "10", "author_name": "test__another_mock", "name": "name_object_mock"}
            mock_db.get_author.return_value = {"name": "name_another_mock", "age": -10, "best_sellers": -50}

            data = get_book.get_info(10)

            # asserts
            mock_db.get_book.assert_called_once_with(10)
            mock_db.get_author.assert_called_once_with(ANY)
            self.assertEquals("name_object_mock", data['title'])


# TODO: Implement a couple of test cases for the get_all method
# Fill the class using mock in your preferred way of mocking
# Check the process.GetBookAuthor.get_all method and get coverage of 100%
class TestGetAllBookAuthor(unittest.TestCase):
    """
    check method get_all
    """

    def test_get_all_books_work(self):
        # side_effect may return several values on consecutive calls (providing a list)
        # We can check sevaral calls using assert_has_calls([call(), ...])
        self.fail("not implemented")

    def test_get_all_books_failing_db(self):
        # Try to mock logger so that we can check the exception is treated
        # with syntax allow multiple patch with patch ... as, patch ... as...
        self.fail("not implemented")


if __name__ == "__main__":
    unittest.main()