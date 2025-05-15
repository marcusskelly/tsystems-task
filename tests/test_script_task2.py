import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
import sys
from script_task2 import get_sites_by_status, main

class TestQuerySitesScript(unittest.TestCase):

    @patch("script_task2.requests.get")
    def test_get_sites_by_status_active(self, mock_get):
        
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "results": [
                {"id": 1, "name": "Site A", "status": {"value": "active"}},
                {"id": 2, "name": "Site B", "status": {"value": "active"}},
            ]
        }
        mock_get.return_value = mock_response

        captured_output = StringIO()
        sys.stdout = captured_output

        get_sites_by_status("active")

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("Sites with status 'active'", output)
        self.assertIn("Site A", output)
        self.assertIn("Site B", output)

    @patch("script_task2.requests.get")
    def test_get_sites_by_status_empty(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"results": []}
        mock_get.return_value = mock_response

        captured_output = StringIO()
        sys.stdout = captured_output

        get_sites_by_status("planned")

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("No sites found with status 'planned'", output)

    @patch("script_task2.get_sites_by_status")
    def test_main_invalid_status(self, mock_fn):
        sys.argv = ["script_task2.py", "invalid"]

        captured_output = StringIO()
        sys.stdout = captured_output

        with self.assertRaises(SystemExit) as cm:
            main()

        sys.stdout = sys.__stdout__
        self.assertEqual(cm.exception.code, 1)
        output = captured_output.getvalue()
        self.assertIn("Invalid status", output)

    def test_main_missing_argument(self):
        sys.argv = ["script_task2.py"]

        captured_output = StringIO()
        sys.stdout = captured_output

        with self.assertRaises(SystemExit) as cm:
            main()

        sys.stdout = sys.__stdout__
        self.assertEqual(cm.exception.code, 1)
        output = captured_output.getvalue()
        self.assertIn("Usage:", output)


if __name__ == "__main__":
    unittest.main()
