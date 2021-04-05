import unittest
from app import Reader


class ReaderTest(unittest.TestCase):
    def setUp(self):
        self.reader = Reader("app/test/test1.txt")

    def test_search_by_period(self):
        self.reader.search_by_period("00:00:01", "13:32:25", "01/Jul/1995", "28/Jul/1995")
        self.assertEqual(29, self.reader.count)

    def test_search_by_period_error(self):
        self.reader.search_by_period("00:00:01", "13:32:25", "01/Jul/1995", "28/Jul/1995")
        self.reader.search_server_error()
        self.assertEqual(11, self.reader.count_error)

    def test_search_by_period_ok(self):
        self.reader.search_by_period("00:00:01", "13:32:25", "01/Jul/1995", "28/Jul/1995")
        self.reader.search_server_ok()
        self.assertEqual(16, self.reader.count_ok)
