import unittest
import requests
import json


if __name__ == "__main__" and __package__ is None:
    from sys import path
    from os.path import dirname as dir

    path.append(dir(path[0]))
    __package__ = "tests"

from workflow import app


class TestAPI(unittest.TestCase):
    def test_request_response(self):
        with app.app_context():
            headers = {'Authorization': app.config['API_AUTH_KEY'], 'Content-Type': "application/json", 'accept': "application/json"}
            payload = {'url': app.config['BASE_IMG']}
            response = requests.post(app.config['API_ENDPOINT'], headers=headers, data=json.dumps(payload), verify=False)
            self.assertEqual(response.status_code, 200)



if __name__ == '__main__':
    unittest.main()