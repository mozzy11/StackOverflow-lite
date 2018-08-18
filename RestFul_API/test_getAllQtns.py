import unittest
import json
from app import create_app

class StackTestCase(unittest.TestCase):


    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client


    def test_add_ans(self):
        res = self.client().post('/api/v1/questions', data= {
                        "id": 2000,
                        "qtnId": 131,
                        "txt": "A boot Camp is a two weeks training for a new Intake"
                    } )
        self.assertEqual(res.status_code, 405)
        respon = self.client().get('/api/v1/questions')
        assert respon.status_code == 200
        self.assertIn('what is Andela', str(respon.data))




if __name__ == "__main__":
    unittest.main()