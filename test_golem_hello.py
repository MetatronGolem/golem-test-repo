
import unittest
from golem_hello import greet

class TestGolemHello(unittest.TestCase):
    def test_greet_returns_correct_string(self):
        self.assertEqual(greet(), "Hello from Golem")

    def test_greet_script_output(self):
        import subprocess
        import sys

        # Run the script and capture output
        result = subprocess.run([sys.executable, 'golem_hello.py'],
                              capture_output=True, text=True)
        self.assertEqual(result.stdout.strip(), "Hello from Golem")

if __name__ == '__main__':
    unittest.main()
