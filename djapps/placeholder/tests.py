from django.test import TestCase
import json
from time import sleep

class TestCasePlaceholder(TestCase):
    def setUp(self) -> None:
        self.GET = "http://localhost:8000/?limit=1"
        self.STATUS = "http://localhost:8000/status/{}/"
        self.RESULT = "http://localhost:8000/result/{}/"

    def test_placeholder_endpoint(self):
        response = self.client.get(self.GET)

        # get worker_id
        self.assertEqual(response.status_code, 200)
        worker_id = response.json().get("id")
        self.assertEqual(type(worker_id), str)

        # check status
        self.assertEqual(
            self.check_status(worker_id),
            "SUCCESS"
        )
        
        
    
    def check_status(self, worker_id: str) -> str|bool:
        print(worker_id)
        stat: bool = False
        for i in range(10):
            response = self.client.get(self.STATUS.format(worker_id))
            self.assertEqual(response.status_code, 200)
            status = response.json().get("status")
            if stat:
                break
            sleep(1)
        else:
            return False
        return stat