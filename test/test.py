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
# from app import app
# import unittest
#
# class FlaskBookshelfTests(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         pass
#
#     @classmethod
#     def tearDownClass(cls):
#         pass
#
#     def setUp(self):
#         # creates a test client
#         self.app = app.test_client()
#         # propagate the exceptions to the test client
#         self.app.testing = True
#
#     def tearDown(self):
#         pass
#
#     def test_home_status_code(self):
#         # sends HTTP GET request to the application
#         # on the specified path
#         result = self.app.get('/')
#
#         # assert the status code of the response
#         self.assertEqual(result.status_code, 200)
#
#     def test_home_data(self):
#         # sends HTTP GET request to the application
#         # on the specified path
#         result = self.app.get('/')
#
#         # assert the response data
#         self.assertEqual(result.data, "Hello World!!!")