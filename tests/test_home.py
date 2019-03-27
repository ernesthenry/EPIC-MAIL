import unittest
import json
from api.views.home_route import app


class BaseTest(unittest.TestCase):
	""" Base Class for test data"""
	def setUp(self):
		self.client = app.test_client()
		
	def test_home(self):
		""" Testing for getting the data at my home route """
		response = self.client.get('/')
		assert b'Welcome to Ernest\'s EPIC MAIL app.' in response.data
		assert response.status_code == 200