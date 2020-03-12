import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from application import create_app, db

class HousingTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.db = db
        self.client = self.app.test_client()
        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            self.db.drop_all()
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TESTS
    """
    def test_health(self):
        res = self.client.get('/')
        data = json.loads(res.data.decode('utf-8'))

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data, 'Healthy')

    def test_get_localities(self):
        res = self.client.get('/localities')
        data = json.loads(res.data.decode('utf-8'))

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
