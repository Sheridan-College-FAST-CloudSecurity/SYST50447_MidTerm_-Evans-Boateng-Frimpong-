import unittest

from fastapi.testclient import \
    TestClient

import app

client = TestClient(app)


# Defining a test class that inherits from the unittest.Testcase
class TestAPI(unittest.TestCase):

    # Function to test if /books endpoint works and returns list of items
    def test_get_books(self):
        response = client.get("/items")  # Send GET reponse to /items
        self.assertEqual(
            response.status_code, 200
        )  # Check if response status is 200 OK
        self.assertIsInstance(
            response.json(), list
        )  # Ensure response status is a list

    # Function to test if /health endpoint works and returns status "ok"
    def test_health_endpoint(self):
        response = client.get("/health")  # Send GET Request to /health
        self.assertEqual(
            response.status_code, 200
        )  # Check if response status is 200 OK
        self.assertEqual(
            response.json(), {"status": "ok"}
        )  # Response should match expected JSON


# Run unit test if the code is executed directly
if __name__ == "__main__":
    unittest.main()