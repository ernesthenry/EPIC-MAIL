import unittest
import json
from api.views.home_route import app
from api.models.user import User
class UserTestCase(unittest.TestCase):

    def setUp(self):
        """initializing method for a unit test"""
        self.client = app.test_client()
        
        self.data = {
                "firstname": "Kato",
                "lastname": "Ernest",
                "email": "henry@gmail.com",
                "password": "070139@He"
                }

    def test_signup_user(self):
        res = self.client.post('/api/v1/auth/signup', content_type="application/json", data=json.dumps(self.data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 201)
        self.assertEqual(response_data['status'], 201)
        self.assertIsInstance(response_data, dict)

    def test_can_signup_user_with_no_data(self):
        
        res = self.client.post('/api/v1/auth/signup', content_type="application/json")
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
            
    def test_register_with_missing_fields(self):
        data = {
                "firstname": "",
                "lastname": "",
                "email": "",
                "password": ""
            }
        res = self.client.post('/api/v1/auth/signup', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        

    def test_email_is_missing(self):
        data = {
                "firstname": "kato",
                "lastname": "ernest",
                "email": "",
                "password": "Bekeplar1234"
        }
        res = self.client.post('/api/v1/auth/signup', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        
    
    def test_first_name_not_string(self):
        data = {
                "firstname": 123,
                "lastname": "ernest",
                "email": "ernest@gmail.com",
                "password": "0701@Henry"
                }
        res = self.client.post('/api/v1/auth/signup', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        

    def test_missing_first_name(self):
        data = {
                "firstname": "",
                "lastname": "Ernest",
                "email": "ernest@gmail.com",
                "password": "0701@Henry"
                }
        res = self.client.post('/api/v1/auth/signup', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        

    def test_missing_last_name(self):
        data = {
                "firstname": "Kato",
                "lastname": "",
                "email": "ernest@gmail.com",
                "password": "0701@Henry"
                }
        res = self.client.post('/api/v1/auth/signup', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        
    def test_last_name_is_not_a_string(self):
        data = {
                "firstname": "Kato",
                "lastname": 2233,
                "email": "ernest@gmail.com",
                "password": "0701@Henry"
                }
        res = self.client.post('/api/v1/auth/signup', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)

    def test_valid_email(self):
        data = {
                "firstname": "Kato",
                "lastname": "Ernest",
                "email": "ernestgmail.com",
                "password": "0701@Hen"
                }
        res = self.client.post('/api/v1/auth/signup', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        

    def test_valid_password(self):
        data = {
                "firstname": "Kato",
                "lastname": "Ernest",
                "email": "ernest@gmail.com",
                "password": "07012345"
                }
        res = self.client.post('/api/v1/auth/signup', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        
    def test_user_already_exists(self):
                
        self.client.post('/api/v1/auth/signup', content_type="application/json", data=json.dumps(self.data))        
        res = self.client.post('/api/v1/auth/signup', content_type="application/json", data=json.dumps(self.data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,409)
        self.assertEqual(response_data['status'], 409)
        self.assertIsInstance(response_data, dict)

    def test_login_user(self):
        data = {
            "firstname": "Kato",
            "lastname": "Ernest",
            "email": "ernest@gmail.com",
            "password": "0701@Henry"
                }
        login_data = {
                       "email":"ernest@gmail.com",
                       "password": "0701@Henry"
                     }
        self.client.post('/api/v1/auth/signup', content_type="application/json", data=json.dumps(data))
        res = self.client.post('/api/v1/auth/login', content_type="application/json", data=json.dumps(login_data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 200)
        self.assertEqual(response_data['status'], 200)
        self.assertIsInstance(response_data, dict)
       
       
    def test_wrong_login_details(self):
        data = {
                "firstname": "waswa",
                "lastname": "hosea",
                "email": "hoseawaswa@gmail.com",
                "password": "0701@Henry"
                }
        login_data = {
                       "email":"hoseaa@gmail.com",
                       "password": "0701@Henry"
                     }
        self.client.post('/api/v1/auth/signup', content_type="application/json", data=json.dumps(data))
        res = self.client.post('/api/v1/auth/login', content_type="application/json", data=json.dumps(login_data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 401)
        self.assertEqual(response_data['status'], 401)
        self.assertIsInstance(response_data, dict)
            
        
