import unittest
from unittest.mock import patch, MagicMock
import yaml
from script_task1 import FilterSitesScript


class TestFilterSitesScript(unittest.TestCase):

    @patch("script_task1.Site")
    def test_run_with_active_sites(self, mock_site_model):
        
        mock_site1 = MagicMock(id=1, name="Site A", status="active")
        mock_site2 = MagicMock(id=2, name="Site B", status="active")

        mock_site_model.objects.filter.return_value = [mock_site1, mock_site2]

        
        script = FilterSitesScript()
        data = {'status': 'active'}
        result_yaml = script.run(data, commit=False)

       
        result_data = yaml.safe_load(result_yaml)

        expected = [
            {'id': 1, 'name': 'Site A', 'status': 'active'},
            {'id': 2, 'name': 'Site B', 'status': 'active'}
        ]

        self.assertEqual(result_data, expected)

    @patch("script_task1.Site")
    def test_run_with_no_matching_sites(self, mock_site_model):
        
        mock_site_model.objects.filter.return_value = []

        script = FilterSitesScript()
        data = {'status': 'planned'}
        result_yaml = script.run(data, commit=False)

        self.assertEqual(result_yaml.strip(), '[]')


if __name__ == "__main__":
    unittest.main()
