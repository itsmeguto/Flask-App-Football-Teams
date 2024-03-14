# tests/test_app.py

import unittest
from flask import current_app
from app import create_app, db

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        # Set up a new app instance for each test
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        # Tear down the app instance after each test
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        # Test the app is actually exists
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        # Test the app is in testing mode
        self.assertTrue(current_app.config['TESTING'])

    def test_home_page(self):
        # Test the home page loads correctly
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome', response.data)  # Change 'Welcome' to a unique word or phrase on your homepage
