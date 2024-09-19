from flask import Flask
from routes import chatbot_routes
from firebase_admin import credentials, initialize_app

# Initialize Flask app
app = Flask(__name__)

# Register routes from routes.py
app.register_blueprint(chatbot_routes)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
