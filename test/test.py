# # # import json
# # # import unittest
# # # from src import main
# # #
# # #
# # # class MyAppCase(unittest.TestCase):
# # #     def setUp(self):
# # #         main.app.config['TESTING'] = True
# # #         self.app = main.app.test_client()
# # #
# # #     def test_dummy(self):
# # #         response = self.app.get("/version")
# # #         data = json.loads(response.get_data(as_text=True))
# # #
# # #         self.assertEqual(data['description'], "dummy-value")
# # import json
# #
# #
# # def test_index(app, client):
# #     res = client.get('/version')
# #     assert res.status_code == 200
# #     expected = {'description': 'pre interview technical test'}
# #     assert expected == json.loads(res.get_data(as_text=True))
#
# # https://damyanon.net/post/flask-series-testing/
#
#
import unittest
import sys

sys.path.append("C:\\natraj\App\\")
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

    def test_version_data(self):
        result = self.app.get('/version')
        assert result.data



if __name__ == '__main__':
    unittest.main()

