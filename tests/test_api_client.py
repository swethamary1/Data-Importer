import unittest
from unittest.mock import patch
from data_importer.api_client import APIClient

class TestAPIClient(unittest.TestCase):
    @patch("data_importer.api_client.requests.get")
    def test_fetch_data(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{"id": "1", "name": "Phone A", "data": {}}]
        client = APIClient("http://example.com")
        data = client.fetch_data()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["id"], "1")

if __name__ == "__main__":
    unittest.main()
