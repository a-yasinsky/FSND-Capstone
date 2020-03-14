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

auth_header_viewer = {
    'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5EaERSVEV5TXprMlJFWkZRakUxTURZNVJVVXpRVUV3TlVNeE5UWXpOelk0TlRRNE56bEVOdyJ9.eyJpc3MiOiJodHRwczovL3NreWRldi5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU2YzViN2EwODQ1NzEwYzkyMjA1OTg3IiwiYXVkIjoiZnNuZC1jYXBzdG9uZSIsImlhdCI6MTU4NDE2Mzc2OSwiZXhwIjoxNTg0MjUwMTY5LCJhenAiOiJKRjFpUFdFbjNXRWdXT201SVhEUmJ4TUtKZUJPdzM4NCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsicmVhZDpob3VzaW5nIl19.JlaNCWH3iWIBe2dmgVmuQqerOy8OogvJzSs4Fm3AfhsuOQ-KaN8NJMIYTCxjyyDxZ-11kuS5mq8jmmei8olaLY-6FAiBfGUL7fsBpTPF6mguAnryUYelJD5fnMtEU-NZYTwMGrt14k9MgiHD_TSAZH7LuBzOO6b8n0fhICVfYpSQp7WmtO-QcPVb52L9UhAkmCLoH3stDHBhDwpcENKRj-HWn00KP6348mQUTgXpfyFgGmboxsePdCdGKckXqWEJuWrw9n7PnelD4CQzq0VZsx_E5pffTU-H_P3CJcAp9fAsdoBh1ZGoS4R80CO0bXd8b5IoytIbFEQbZ48B4fXQRg"
}
auth_header_manager = {
  'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5EaERSVEV5TXprMlJFWkZRakUxTURZNVJVVXpRVUV3TlVNeE5UWXpOelk0TlRRNE56bEVOdyJ9.eyJpc3MiOiJodHRwczovL3NreWRldi5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU2OGMzNmRjMGNlMTYwZDk4NDdhMjU1IiwiYXVkIjoiZnNuZC1jYXBzdG9uZSIsImlhdCI6MTU4NDE2Mzg0NiwiZXhwIjoxNTg0MjUwMjQ2LCJhenAiOiJKRjFpUFdFbjNXRWdXT201SVhEUmJ4TUtKZUJPdzM4NCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsicGF0Y2g6aG91c2luZyIsInBvc3Q6aG91c2luZyIsInJlYWQ6aG91c2luZyJdfQ.TBUTZRlPyjei5qz71u21utEenlNM4uV98DaXtR69wKC_Wtvo6tEcYd7tcnCWanOc1Mqa-9zWrYlqh59_XLpFXJbNJ0Gfc_1m5M4OgMri4PV6-j4AWhtrO2Ux5kno1rGWRgEQ1iJmx2tgF9Copj2KkPt_csWlxEIYBIQYggrjrZwoxNp_sHacl_rsj4_lHF6K1h9QPjiFKLpwg5QVSnpzulQzkSMN7iRABv7hOWPCmdsAeAgwkm8i11TqXlgnM6iv8hBOCbBjxUlrai4zNfHKragL1yyzmMLbSfL2St3s-xNmu_KLORZmY06gKdOCky04sxYUIcoGqcu5La0BEEzKWw"
}
auth_header_admin = {
  'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5EaERSVEV5TXprMlJFWkZRakUxTURZNVJVVXpRVUV3TlVNeE5UWXpOelk0TlRRNE56bEVOdyJ9.eyJpc3MiOiJodHRwczovL3NreWRldi5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU2OGMzYmFjMGNlMTYwZDk4NDdhMzI2IiwiYXVkIjoiZnNuZC1jYXBzdG9uZSIsImlhdCI6MTU4NDE2MzkyNCwiZXhwIjoxNTg0MjUwMzI0LCJhenAiOiJKRjFpUFdFbjNXRWdXT201SVhEUmJ4TUtKZUJPdzM4NCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmhvdXNpbmciLCJwYXRjaDpob3VzaW5nIiwicG9zdDpob3VzaW5nIiwicmVhZDpob3VzaW5nIl19.PDdYPKTinPnQgcIXx2ZS5MKs943f5wCxZTkK66DEsPUK5E3bZDYBku4xsNrtaFxKV8blIy1lftyee6bRK_uOlDB3teMNX3GzDHAfG5ELDSSDkghZJf1L6OgwdrLy-RUF4EGfIWrf7flky6MfbfS6HezRmED9ybV92JcMag4pn_UX0mA2RlDDBrDDlge61S414XwibRp14539lye5TlUQhl7oPbYjefQ6G2qaYy2Na14NaWLeXTvZv7k5Wx6PsgGHiebEkboVXLRiVsdi8QQta2Mz7y1cYcl-mUamnc67qT-MgkJh6TNveCKp9_ACIrYIV7gwy4Bok3Kndfe4i147xg"
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

    def test_get_localities(self):
        res = self.client.get('/localities', headers=auth_header_viewer)
        data = json.loads(res.data.decode('utf-8'))

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['localities'])

    def test_get_housing_by_locality(self):
        res = self.client.get('/localities/1/housing',
                            headers=auth_header_viewer)
        data = json.loads(res.data.decode('utf-8'))

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_housing'])
        self.assertTrue(len(data['housing']))

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
        res = self.client.get('/housing/{}'.format(housing_id),
                                headers=auth_header_viewer)
        data = json.loads(res.data.decode('utf-8'))

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['housing']['id'], housing_id)

    def test_404_get_housing_not_exist(self):
        res = self.client.get('/housing/1000', headers=auth_header_viewer)
        data = json.loads(res.data.decode('utf-8'))

        self.assertEqual(res.status_code, 404)

    def test_get_housing(self):
        res = self.client.get('/housing', headers=auth_header_viewer)
        data = json.loads(res.data.decode('utf-8'))

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_housing'])
        self.assertTrue(len(data['housing']))

    def test_search_housing(self):
        res = self.client.get('/housing/search?q=searchval',
                                headers=auth_header_viewer)
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
