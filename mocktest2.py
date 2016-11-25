import unittest
import requests
from mock import patch


class PatchExample(unittest.TestCase):
    @patch('requests.get')
    def test_something(self, mock_get):
        r = requests.get('http://google.com/')
        self.assertEqual(mock_get.called, True)
        (url), kwargs = mock_get.call_args
        print url, kwargs
        self.assertEqual(url[0], 'http://google.com/')

if __name__ == '__main__':
    unittest.main()
