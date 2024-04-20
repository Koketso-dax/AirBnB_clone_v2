from flask import Flask

# Create a Flask app instance
app = Flask(__name__)

# Route for the homepage
@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'

# Route for /hbnb
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
