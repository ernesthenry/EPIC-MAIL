#api/controllers
from flask import jsonify
class Home:
    def home(self):
        """A welcoming route to my api"""
        return jsonify({
            'data': 'Welcome to Ernest\'s EPIC MAIL app.',
                'status': 200
                }), 200