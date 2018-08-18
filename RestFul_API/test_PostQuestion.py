import unittest
import json
from app import create_app

class StackTestCase(unittest.TestCase):


    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client


    def test_add_ans(self):
        respon = self.client().post( '/api/v1/questions',data = json.dumps({
            'id': 202,
            'txt': 'is this queston Returned',
            'Poster': 'Arnold'
                    } ) ,content_type='application/json', )
        data = json.loads(respon.get_data(as_text=True))
        assert respon.status_code == 200
        assert data['id'] == 202



if __name__ == "__main__":
    unittest.main()