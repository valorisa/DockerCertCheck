import unittest
from unittest.mock import patch
import docker_cert_check

class TestDockerCertCheck(unittest.TestCase):

    @patch('subprocess.run')
    def test_check_dependencies(self, mock_run):
        mock_run.return_value.returncode = 0
        docker_cert_check.check_dependencies()
        mock_run.assert_called_with(["which", "codesign"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    @patch('subprocess.check_output')
    @patch('subprocess.run')
    def test_extract_certificates(self, mock_run, mock_check_output):
        mock_run.return_value.returncode = 0
        mock_check_output.return_value = "certificate details"
        binary_file = "/path/to/binary"
        details, name = docker_cert_check.extract_certificates(binary_file)
        self.assertEqual(details, "certificate details")
        self.assertEqual(name, "binary")

if __name__ == '__main__':
    unittest.main()
