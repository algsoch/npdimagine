import unittest
from src.tasks import process_data

class TestTasks(unittest.TestCase):
    def test_process_data(self):
        test_input = {"key": "value"}
        result = process_data(test_input)
        self.assertIsInstance(result, dict)
        self.assertIn("processed", result)

if __name__ == "__main__":
    unittest.main()
