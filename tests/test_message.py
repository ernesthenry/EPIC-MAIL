import unittest
import json
from api.views.home_route import app
from api.models.message import Message, user_messages
from api.models.user import User, user_data


class MessageTestCase(unittest.TestCase):

    def setUp(self):
        """initializing method for a unit test"""
        self.client = app.test_client()
        
        self.user_data = {
            "firstname": "Kato",
            "lastname": "Ernest",
            "email": "ernest@gmail.com",
            "password": "ernest38"
                }
            
        self.user_login_data = {
                       "email":"ernest@gmail.com",
                       "password": "ernest38"
                     }

        self.message_data = {
            "subject": "teteyyer hrrur ",
            "message": "hrjrrjk jrjrir jkriror",
            "ParentMessageID": "121",
            "receiver": "kambugu"
        }


        self.data = {}


    def test_create_message(self):
        self.client.post('/api/v1/auth/signup', content_type="application/json", data=json.dumps(self.user_data))        
        res1 = self.client.post('/api/v1/auth/login', content_type="application/json", data=json.dumps(self.user_login_data))
        self.assertEqual(res1.status_code, 200)
        res = self.client.post('/api/v1/messages', content_type="application/json", data=json.dumps(self.message_data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 201)
        self.assertEqual(response_data['status'], 201)
        self.assertIsInstance(response_data, dict)

    def test_create_message_without_data(self):
        self.client.post('/api/v1/auth/signup', content_type="application/json", data=json.dumps(self.user_data))        
        res1 = self.client.post('/api/v1/auth/login', content_type="application/json", data=json.dumps(self.user_login_data))
        self.assertEqual(res1.status_code, 200)
        res = self.client.post('/api/v1/messages', content_type="application/json")
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)


    def test_create_message_without_subject(self):
        data = {
            "subject": "",
            "message": "Ernest",
            "ParentMessageID": "121" 
        }
        self.client.post('/api/v1/auth/signup', content_type="application/json", data=json.dumps(self.user_data))        
        res1 = self.client.post('/api/v1/auth/login', content_type="application/json", data=json.dumps(self.user_login_data))
        self.assertEqual(res1.status_code, 200)
        res = self.client.post('/api/v1/messages', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)

    def test_create_message_empty_message(self):
        data = {
            "subject": "Welcome to EPIC MAIL",
            "ParentMessageID": "121"
        }
        self.client.post('/api/v1/auth/signup', content_type="application/json", data=json.dumps(self.user_data))        
        res1 = self.client.post('/api/v1/auth/login', content_type="application/json", data=json.dumps(self.user_login_data))
        self.assertEqual(res1.status_code, 200)
        res = self.client.post('/api/v1/messages', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)

    def test_create_message_missing_subject_field(self):
        data = {
            "message": "Joseph",
            "ParentMessageID": "121" 
        }
        self.client.post('/api/v1/auth/signup', content_type="application/json", data=json.dumps(self.user_data))        
        res1 = self.client.post('/api/v1/auth/login', content_type="application/json", data=json.dumps(self.user_login_data))
        self.assertEqual(res1.status_code, 200)
        res = self.client.post('/api/v1/messages', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)

    def test_duplicate_message(self):
            self.client.post('/api/v1/auth/signup', content_type="application/json", data=json.dumps(self.user_data))        
            res1 = self.client.post('/api/v1/auth/login', content_type="application/json", data=json.dumps(self.user_login_data))
            self.assertEqual(res1.status_code, 200)
            self.client.post('/api/v1/messages', content_type="application/json", data=json.dumps(self.message_data))
            res = self.client.post('/api/v1/messages', content_type="application/json", data=json.dumps(self.message_data))
            response_data = json.loads(res.data.decode())
            self.assertEqual(res.status_code, 409)
            self.assertEqual(response_data['status'], 409)
            self.assertIsInstance(response_data, dict)


    def test_get_message(self):
            self.client.post('/api/v1/auth/signup', content_type="application/json", data=json.dumps(self.user_data))        
            res1 = self.client.post('/api/v1/auth/login', content_type="application/json", data=json.dumps(self.user_login_data))
            self.assertEqual(res1.status_code, 200)
            self.client.post('/api/v1/messages', content_type="application/json", data=json.dumps(self.message_data))
            res = self.client.get('/api/v1/messages/2', content_type="application/json", data=json.dumps(self.message_data))
            response_data = json.loads(res.data.decode())
            self.assertEqual(res.status_code, 404)
           
    def test_get_message_not_existing(self):
            self.client.post('/api/v1/auth/signup', content_type="application/json", data=json.dumps(self.user_data))        
            res1 = self.client.post('/api/v1/auth/login', content_type="application/json", data=json.dumps(self.user_login_data))
            self.assertEqual(res1.status_code, 200)
            self.client.post('/api/v1/messages', content_type="application/json", data=json.dumps(self.message_data))
            res = self.client.get('/api/v1/messages/3', content_type="application/json", data=json.dumps(self.message_data))
            response_data = json.loads(res.data.decode())
            self.assertEqual(res.status_code, 404)
            self.assertEqual(response_data['status'], 404)
            self.assertIsInstance(response_data, dict)

    def test_no_existing_deleted_message(self):
            self.client.post('/api/v1/auth/signup', content_type="application/json", data=json.dumps(self.user_data))        
            resp = self.client.post('/api/v1/auth/login', content_type="application/json", data=json.dumps(self.user_login_data))
            self.assertEqual(resp.status_code, 200)
            self.client.post('/api/v1/messages', content_type="application/json",
                headers={'Authorization': 'Bearer ' + self.token}, data=json.dumps(self.message_data))
            res = self.client.delete('/api/v1/messages/3', content_type="application/json", data=json.dumps(self.message_data))
            response_data = json.loads(res.data.decode())
            self.assertEqual(res.status_code, 404)
            self.assertEqual(response_data['status'], 404)
            self.assertIsInstance(response_data, dict)


    def test_get_all_sent(self):
        self.client.post('/api/v1/auth/signup', content_type="application/json", data=json.dumps(self.user_data))        
        res1 = self.client.post('/api/v1/auth/login', content_type="application/json", data=json.dumps(self.user_login_data))
        self.assertEqual(res1.status_code, 200)
        self.client.post('/api/v1/messages', content_type="application/json", data=json.dumps(self.message_data))
        res = self.client.get('/api/v1/messages/sent', content_type="application/json", data=json.dumps(self.message_data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 200)
        self.assertEqual(response_data['status'], 200)
        self.assertIsInstance(response_data, dict)


    def test_get_all_sent_empty_records(self):
        self.client.post('/api/v1/auth/signup', content_type="application/json", data=json.dumps(self.user_data))        
        res1 = self.client.post('/api/v1/auth/login', content_type="application/json", data=json.dumps(self.user_login_data))
        self.assertEqual(res1.status_code, 200)
        res = self.client.get('/api/v1/messages/sent', content_type="application/json",
            headers={'Authorization': 'Bearer ' + self.token}, data=json.dumps(self.message_data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 404)
        self.assertEqual(response_data['status'], 404)
        self.assertIsInstance(response_data, dict)


    def tearDown(self):
        user_messages.clear()

