import unittest
import requests
from mock import patch, Mock


class PatchExample(unittest.TestCase):
    @patch('requests.get')
    def test_something(self, mock_get):
        mock_get.side_effect = requests.exceptions.HTTPError('Unable to connect')

        #mock_get.side_effect = requests.HTTPError(Mock(return_value={'status':404}), 'not found')
        r = requests.get('http://google.com/')
        self.assertEqual(mock_get.called, True)
        (url), kwargs = mock_get.call_args
        print url, kwargs
        self.assertEqual(url[0], 'http://google.com/')

if __name__ == '__main__':
    unittest.main()