import unittest
from unittest.mock import patch, MagicMock
from io import StringIO

# Importing functions from your script
from portscangui import scanPort, updateResult, startScan, saveScan

class TestPortScanner(unittest.TestCase):

    @patch('portscangui.scanPort')
    @patch('portscangui.updateResult')  # Patching the updateResult function
    def test_updateResult(self, mock_update_result, mock_scanPort):
        # Set up initial values
        ports = [80, 443]
        ip_f = 1024
        target = "localhost"
        expected_result = f" [ {len(ports)} / {ip_f} ] ~ {target}"

        # Mock the GUI update function
        mock_update_gui = MagicMock()

        # Call the function to be tested
        updateResult()

        # Check if the GUI update function was called with the correct arguments
        mock_update_gui.assert_called_once_with(expected_result)

    # Add other test methods here...

if __name__ == '_main_':
    unittest.main()