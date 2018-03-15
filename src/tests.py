'''
    magic-cards tests

    unittesting class
'''
import os
import unittest

import dao


class DaoTesting(unittest.TestCase):

    def setUp(self):
        self.tmpfile = '/tmp/hello'

    def test_empty_query(self):
        res = list(dao.get_cards('alpha'))
        self.assertEqual(len(res), 0, 'empty query')

    def test_non_empty_query(self):
        res = list(dao.get_cards(1))
        self.assertNotEqual(len(res), 0, 'empty query')

    def test_read_inexistant(self):
        with self.assertRaises(FileNotFoundError):
            dao.read_file('/thisfileshouldnexist.yxy')

    def test_write_file(self):
        dao.write_file('hello', self.tmpfile)
        self.assertTrue(os.path.exists(self.tmpfile), 'writting file')

    def test_read_file(self):
        dao.write_file('hello', self.tmpfile)
        res = dao.read_file(self.tmpfile)
        self.assertEqual('hello', res, 'reading file')


if __name__ == '__main__':
    unittest.main()
