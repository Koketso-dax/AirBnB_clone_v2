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

# Route for /c/<text>
@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    # Replace underscores with spaces
    text = text.replace('_', ' ')
    return 'C {}'.format(text)

# Route for /python/<text>
@app.route('/python/<text>', strict_slashes=False)
def display_python(text='is_cool'):
    # Replace underscores with spaces
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)

# Route for /number/<n>
@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    return '{} is a number'.format(n)

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
