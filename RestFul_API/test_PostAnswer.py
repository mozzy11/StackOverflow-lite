
import unittest
import json
from app import create_app

class StackTestCase(unittest.TestCase):


    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client


    def test_add_ans(self):
        respon = self.client().post( 'questions/101/answers',data = json.dumps({
                        "id": 2000,
                        "qtnId": 131,
                        "txt": "A boot Camp is a two weeks training for a new Intake"
                    } ) ,content_type='application/json', )
        data = json.loads(respon.get_data(as_text=True))
        assert respon.status_code == 200
        assert data['qtnId'] == 101



if __name__ == "__main__":
    unittest.main()