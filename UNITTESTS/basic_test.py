import unittest
import ao_pyth as ao
import os
api_key = os.getenv("API_KEY")  

class TestApi(unittest.TestCase):

    def test_kennel_create(self):
        arch = ao.Arch([1, 1, 1], [1], api_key=api_key, kennel_id="unittestcase-1", stage="prod")
        print(arch.api_status)
        self.assertTrue(
            "newly created Kennel" in arch.api_status or "Oops-- a kennel with this name" in arch.api_status,
        )
        
if __name__ == '__main__':
    unittest.main()