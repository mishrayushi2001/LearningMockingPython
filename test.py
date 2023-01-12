import unittest
from mycalender import requests, get_holidays
from unittest.mock import patch

class TestCalendar(unittest.TestCase):
    
    @patch.object(requests, 'get',side_effect= requests.exceptions.Timeout)
    def test_get_holidays_timeout(self, mock_requests):
        # with patch('mycalender.requests') as mock_requests:
            # mock_requests.get.side_effect = Timeout
            with self.assertRaises(requests.exceptions.Timeout):
                # from mycalender import get_holidays
                get_holidays()
                # mock_requests.get.assert_called_once()

if __name__ == '__main__':
    unittest.main()