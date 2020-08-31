import unittest
import sys
import os
cwd = os.getcwd()
sys.path.append(cwd)
from src import main


class HomeVersionPage(unittest.TestCase):

    def setUp(self):
        main.app.config['TESTING'] = True
        self.app = main.app.test_client()

    def test_home_status_code(self):
        response = self.app.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_home_data(self):
        result = self.app.get('/')
        assert result.data == b'<h1> ANZ pre Interview Solution</h1> <p> <p><a href=../version>click here to navigate to /version page</a></p></p>'


    def test_version_status_code(self):
        response = self.app.get('/version', content_type='html/text')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
