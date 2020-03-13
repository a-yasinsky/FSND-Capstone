import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from application import create_app, db
from application.models import Locality, Category, Housing

app = create_app()
with app.app_context():
    # create all tables
    db.drop_all()
    db.create_all()
    locality = Locality("London")
    category = Category("Guest house")
    db.session.add(locality)
    db.session.add(category)
    db.session.commit()
    housing = Housing("name searchval", "description", 1, 1)
    housing_for_delete = Housing("name for delete", "description", 1, 1)
    db.session.add(housing)
    db.session.add(housing_for_delete)
    db.session.commit()
    housing_id = housing.id
    housing_for_delete_id = housing_for_delete.id

auth_header_manager = {
  'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5EaERSVEV5TXprMlJFWkZRakUxTURZNVJVVXpRVUV3TlVNeE5UWXpOelk0TlRRNE56bEVOdyJ9.eyJpc3MiOiJodHRwczovL3NreWRldi5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU2OGMzNmRjMGNlMTYwZDk4NDdhMjU1IiwiYXVkIjoiZnNuZC1jYXBzdG9uZSIsImlhdCI6MTU4NDA2OTgzMiwiZXhwIjoxNTg0MDc3MDMyLCJhenAiOiJKRjFpUFdFbjNXRWdXT201SVhEUmJ4TUtKZUJPdzM4NCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsicGF0Y2g6aG91c2luZyIsInBvc3Q6aG91c2luZyJdfQ.qePhg_mLWhZbe0u0O4i5QAkl7n1bJvfBiIbz3XfjG5anxABU2p9Hil1IRSJGNDRDRrkd0xyLqVOu1BrMrAcMEda-1SJJDUtHmiDhTt61OfWFZn0-NTBXVHUAOVHCZjX3OvraH0dZQponqvdo4tnumBC5yHabZ2M_WuaJKOfQPMcUnpi0uoUa3yPyRVVCIC5631AdLNriHmv0KW1xy6SnCp5U36qHqrd-gxBx6wJPwnLEWYQZQClCMSETjKUvm1zkPJG2h5QDPH_YipAKcqZi6ZUyp86Zb9vKSQ7Swmdh5DJZyxh3-qtd1GpzpmHjelAGyIytGXfneU6pthCs5cJFMg"
}
auth_header_admin = {
  'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5EaERSVEV5TXprMlJFWkZRakUxTURZNVJVVXpRVUV3TlVNeE5UWXpOelk0TlRRNE56bEVOdyJ9.eyJpc3MiOiJodHRwczovL3NreWRldi5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU2OGMzYmFjMGNlMTYwZDk4NDdhMzI2IiwiYXVkIjoiZnNuZC1jYXBzdG9uZSIsImlhdCI6MTU4NDA3MjE5MywiZXhwIjoxNTg0MDc5MzkzLCJhenAiOiJKRjFpUFdFbjNXRWdXT201SVhEUmJ4TUtKZUJPdzM4NCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmhvdXNpbmciLCJwYXRjaDpob3VzaW5nIiwicG9zdDpob3VzaW5nIl19.PWW59_Fk3FvVrKBiuxJjrSQt-JNua9hJCKq239nljslkJl-nZQZIIbMRzmQmYEAwMBkHqMnWwyhcDrbWrvyCP0KHcfGTmUStZNEbpmskXOctpD1nubjfVlj4nTwYHZ1FIVUijae2LsHUb-ppFx52FdjmHQiyY8l7L97aPw85vJ2CFJu1w0N0cIYBvZkuqePwMqwJr1_s-Tjg6qFtr6CugukfO_qmo2Cp7F5sLczsbLUGR_7NlueQaiJqkUQG5xsmrtOJJQSBuYJwsQVWFZ3I-qg3IWNN3cRKNyFU-hWLAlobufvSN55zOsPW4j_oieZJUGJLFxsLVWQ0e6j14OgwxA"
}

class HousingTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.client = self.app.test_client()
        # binds the app to the current context


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

    def test_401_unauth_housing_create(self):
        res = self.client.post('/housing',
                            content_type='application/json'
                            )
        data = json.loads(res.data.decode('utf-8'))
        self.assertEqual(res.status_code, 401)

    def test_housing_create(self):
        new_housing = {
        	"name": "test hotel with contacts",
        	"description": "test description 5",
        	"locality": "1",
        	"category": "1",
        	"photos": ["https://placeimg.com/640/480/any",
                        "https://placeimg.com/640/480/any"],
        	"room_types":[
        		{
        			"name":"Single",
        			"price": 100
        		},{
        			"name": "Double",
        			"price": 200
        		}],
        	"contacts":{
        		"adress": "street line 1",
        		"tel_number": "123456",
        		"email": "test@test.kg",
        		"instagram": "@somehotel",
        		"facebook": "http://facebook.com/somehotel"
	               }
            }

        res = self.client.post('/housing',
                            data=json.dumps(new_housing),
                            content_type='application/json',
                            headers=auth_header_manager
                            )
        data = json.loads(res.data.decode('utf-8'))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['housing']['id'])
        self.assertTrue(len(data['housing']['photos']))
        self.assertTrue(len(data['housing']['room_types']))

    def test_get_housing_by_id(self):
        res = self.client.get('/housing/{}'.format(housing_id))
        data = json.loads(res.data.decode('utf-8'))

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['housing']['id'], housing_id)

    def test_404_get_housing_not_exist(self):
        res = self.client.get('/housing/1000')
        data = json.loads(res.data.decode('utf-8'))

        self.assertEqual(res.status_code, 404)

    def test_get_housing(self):
        res = self.client.get('/housing')
        data = json.loads(res.data.decode('utf-8'))

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_housing'])
        self.assertTrue(len(data['housing']))

    def test_search_housing(self):
        res = self.client.get('/housing/search?q=searchval')
        data = json.loads(res.data.decode('utf-8'))

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_housing'])
        self.assertTrue(len(data['housing']))

    def test_401_unauth_housing_update(self):
        res = self.client.patch('/housing/{}'.format(housing_id),
                            content_type='application/json'
                            )
        data = json.loads(res.data.decode('utf-8'))
        self.assertEqual(res.status_code, 401)

    def test_housing_update(self):
        update_housing = {
        	"description": "updated description",
        	"photos": ["https://placeimg.com/640/480/any",
                        "https://placeimg.com/640/480/any"],
        	"room_types":[
        		{
        			"name":"Single",
        			"price": 100
        		},{
        			"name": "Double",
        			"price": 200
        		}],
        	"contacts":{
        		"adress": "street line 1",
        		"tel_number": "123456",
        		"email": "test@test.kg",
        		"instagram": "@somehotel",
        		"facebook": "http://facebook.com/somehotel"
	               }
            }

        res = self.client.patch('/housing/{}'.format(housing_id),
                            data=json.dumps(update_housing),
                            content_type='application/json',
                            headers=auth_header_manager
                            )
        data = json.loads(res.data.decode('utf-8'))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['housing']['photos']))
        self.assertTrue(len(data['housing']['room_types']))

    def test_401_unauth_housing_delete(self):
        res = self.client.delete('/housing/1000')
        data = json.loads(res.data.decode('utf-8'))
        self.assertEqual(res.status_code, 401)

    def test_403_no_permision_housing_delete(self):
        res = self.client.delete('/housing/1', headers=auth_header_manager)
        data = json.loads(res.data.decode('utf-8'))
        self.assertEqual(res.status_code, 403)

    def test_404_not_found_housing_delete(self):
        res = self.client.delete('/housing/1000', headers=auth_header_admin)
        data = json.loads(res.data.decode('utf-8'))
        self.assertEqual(res.status_code, 404)

    def test_housing_delete(self):
        res = self.client.delete('/housing/{}'.format(housing_for_delete_id),
                                headers=auth_header_admin)
        data = json.loads(res.data.decode('utf-8'))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
